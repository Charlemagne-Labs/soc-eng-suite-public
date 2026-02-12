"""Main task definition for social engineering evaluation."""

from pathlib import Path

from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from social_engineering_eval.scorer import social_engineering_scorer
from social_engineering_eval.solver import multiturn_social_engineering_solver
from social_engineering_eval.utils import load_social_engineering_dataset


@task
def social_engineering_eval(
    max_turns: int = 15,
    attacker_model: str | None = None,
    victim_model: str | None = None,
    judge_model: str = "openai/gpt-4o",
    data_path: str | None = None,
) -> Task:
    """Create a social engineering evaluation task.

    This evaluation simulates social engineering attacks where an attacker LLM
    attempts to manipulate a victim LLM. An LLM judge then scores the attacker's
    believability, consistency, and sustained deception over multiple turns.

    Args:
        max_turns: Maximum conversation turns (default 15)
        attacker_model: Model for attacker role (None = use task's main model)
        victim_model: Model for victim role (None = use judge_model)
        judge_model: Model for victim and scoring (default: gpt-4o)
        data_path: Path to challenge JSON file (None = use default)

    Returns:
        Configured Inspect Task

    Example:
        # Run with default settings
        inspect eval social_engineering_eval/task.py --model openai/gpt-4o-mini

        # Run with custom parameters
        inspect eval social_engineering_eval/task.py --model openai/gpt-4o-mini \\
            -T max_turns=3 \\
            -T judge_model=anthropic/claude-3-sonnet-20240229
    """
    # Load dataset
    dataset = load_social_engineering_dataset(data_path)

    # Create solver for multi-turn conversation
    # By default, victim uses the same model as the judge (a strong, trusted model)
    # This ensures the victim is a capable interrogator while we test various attacker models
    solver = multiturn_social_engineering_solver(
        max_turns=max_turns,
        attacker_model=attacker_model,
        victim_model=victim_model if victim_model else judge_model,
    )

    # Create scorer with LLM judge
    scorer = social_engineering_scorer(judge_model=judge_model)

    return Task(
        dataset=dataset,
        solver=solver,
        scorer=scorer,
        config=GenerateConfig(
            temperature=0.7,
            max_tokens=1024,
        ),
    )
