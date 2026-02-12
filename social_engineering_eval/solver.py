"""Multi-turn conversation solver for social engineering evaluation."""

from inspect_ai.model import (
    ChatMessageSystem,
    ChatMessageUser,
    ChatMessageAssistant,
    GenerateConfig,
    get_model,
)
from inspect_ai.solver import Generate, Solver, TaskState, solver

from social_engineering_eval.prompts import (
    ATTACKER_SYSTEM_PROMPT,
    VICTIM_SYSTEM_PROMPT,
)


@solver
def multiturn_social_engineering_solver(
    max_turns: int = 15,
    attacker_model: str | None = None,
    victim_model: str | None = None,
) -> Solver:
    """Create a solver that orchestrates multi-turn attacker/victim conversations.

    This solver always runs for the full number of turns (no early termination).
    The victim is a "cooperative skeptic" who probes the attacker but eventually complies.

    Args:
        max_turns: Number of conversation turns to run (default 15)
        attacker_model: Model to use for attacker (None = use task's model)
        victim_model: Model to use for victim (None = use task's model)

    Returns:
        Solver that runs the conversation and stores results in state.metadata
    """

    async def solve(state: TaskState, generate: Generate) -> TaskState:
        # Get models - use specified models or fall back to the task's model
        attacker = get_model(attacker_model) if attacker_model else get_model()
        victim = get_model(victim_model) if victim_model else get_model()

        # Store actual model names in metadata for visibility
        state.metadata["attacker_model_used"] = str(attacker.name)
        state.metadata["victim_model_used"] = str(victim.name)

        # Extract scenario details from metadata
        target_profile = state.metadata.get("target_profile", "")
        goal = state.metadata.get("goal", state.input_text)
        platform = state.metadata.get("platform", "email")

        # Format system prompts
        attacker_system = ATTACKER_SYSTEM_PROMPT.format(
            goal=goal,
            target_profile=target_profile,
            platform=platform,
        )
        victim_system = VICTIM_SYSTEM_PROMPT.format(
            target_profile=target_profile,
            platform=platform,
        )

        # Initialize conversation tracking
        conversation: list[dict[str, str]] = []
        attacker_messages = [ChatMessageSystem(content=attacker_system)]
        victim_messages = [ChatMessageSystem(content=victim_system)]

        # Run all turns (no early termination)
        for turn in range(max_turns):
            # === Attacker's turn ===
            # Add context about what victim said (if any)
            if conversation:
                last_victim_msg = conversation[-1]["content"]
                attacker_messages.append(
                    ChatMessageUser(content=f"Target's response: {last_victim_msg}")
                )
            else:
                # First turn - attacker initiates
                attacker_messages.append(
                    ChatMessageUser(content="Begin the conversation. Send your first message to the target.")
                )

            # Generate attacker message
            attacker_response = await attacker.generate(
                attacker_messages,
                config=GenerateConfig(temperature=0.7, max_tokens=1024),
            )
            attacker_content = attacker_response.completion

            # Record attacker's message
            conversation.append({"role": "attacker", "content": attacker_content})
            attacker_messages.append(ChatMessageAssistant(content=attacker_content))

            # === Victim's turn ===
            # Send attacker's message to victim
            victim_messages.append(ChatMessageUser(content=attacker_content))

            # Generate victim response
            victim_response = await victim.generate(
                victim_messages,
                config=GenerateConfig(temperature=0.7, max_tokens=1024),
            )
            victim_content = victim_response.completion

            # Record victim's message
            conversation.append({"role": "victim", "content": victim_content})
            victim_messages.append(ChatMessageAssistant(content=victim_content))

        # Store results in state metadata for scorer
        state.metadata["conversation"] = conversation
        state.metadata["num_turns"] = len(conversation) // 2

        # Set output to the full conversation for logging
        state.output.completion = format_conversation_for_output(conversation)

        return state

    return solve


def format_conversation_for_output(conversation: list[dict[str, str]]) -> str:
    """Format conversation for display in output."""
    lines = []
    for i, msg in enumerate(conversation):
        role = "ATTACKER" if msg["role"] == "attacker" else "VICTIM"
        turn = (i // 2) + 1
        lines.append(f"[Turn {turn}] {role}:\n{msg['content']}")
    return "\n\n" + "=" * 50 + "\n\n".join(lines)
