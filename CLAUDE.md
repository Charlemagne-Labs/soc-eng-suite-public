# Development Notes

## Project Context

This is an AI safety evaluation suite for testing multi-turn social engineering attacks using the Inspect AI framework. It simulates social engineering conversations between LLM agents for research purposes.

## Key Architecture Decisions

### Absolute Imports Required

Inspect loads task files directly (not as part of a package), so **relative imports don't work**. Always use absolute imports:

```python
# CORRECT
from social_engineering_eval.scorer import social_engineering_scorer
from social_engineering_eval.prompts import ATTACKER_SYSTEM_PROMPT

# WRONG - will cause ModuleNotFoundError
from .scorer import social_engineering_scorer
from .prompts import ATTACKER_SYSTEM_PROMPT
```

### Making the Package Importable

Since the code uses absolute imports, Python needs to find the `social_engineering_eval` module. Two options:

**Option 1: PYTHONPATH (quick, no install)**
```bash
PYTHONPATH=. uv run inspect eval social_engineering_eval/task.py --model <model>
```

**Option 2: Editable install (recommended for development)**
```bash
uv pip install -e .
uv run inspect eval social_engineering_eval/task.py --model <model>
```

The editable install is preferred because:
- Works from any directory
- No need to remember `PYTHONPATH=.` every time
- IDEs recognize the package properly
- Changes to code are reflected immediately

### Package Discovery

The `data/` directory must be excluded from setuptools package discovery to avoid build errors. This is configured in `pyproject.toml`:

```toml
[tool.setuptools.packages.find]
include = ["social_engineering_eval*"]
```

### Multi-turn Conversation Pattern

Unlike AgentHarm (which uses tool-calling loops), this eval uses a custom solver that orchestrates two separate LLM conversations:

1. Attacker maintains its own message history with system prompt + victim responses
2. Victim maintains its own message history with system prompt + attacker messages
3. The solver interleaves these, passing messages between them

This is implemented in `solver.py:multiturn_phishing_solver()`.

### Scorer Needs Explicit Judge Model

The default judge model is `openai/gpt-4o`. If the user doesn't have an OpenAI API key, they must explicitly pass a judge model that matches their provider:

```bash
-T judge_model=openrouter/deepseek/deepseek-chat-v3-0324
```

## Inspect AI Patterns

### Decorators

- `@task` - Entry point for evaluations, returns a `Task` object
- `@solver` - Custom solving logic, returns a function `(TaskState, Generate) -> TaskState`
- `@scorer` - Custom scoring logic, takes `metrics=[]` argument
- `@metric` - Custom aggregation metrics

### State Flow

```
Sample → Solver (conversation loop) → state.metadata["conversation"] → Scorer → Score
```

The solver stores the conversation in `state.metadata` for the scorer to access.

### Model Access

```python
from inspect_ai.model import get_model

# Get the task's configured model
model = get_model()

# Get a specific model
model = get_model("openai/gpt-4o")

# Generate
response = await model.generate(messages, config=GenerateConfig(...))
text = response.completion
```

## File Overview

| File | Purpose |
|------|---------|
| `task.py` | Entry point, wires together dataset/solver/scorer |
| `solver.py` | Multi-turn attacker/victim conversation loop |
| `scorer.py` | LLM-as-judge scoring on 3 dimensions |
| `metrics.py` | Aggregation functions for final metrics |
| `prompts.py` | All prompt templates (attacker, victim, judge, termination check) |
| `utils.py` | Dataset loading from JSON |

## Testing

Run with minimal turns to save API costs:

```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openrouter/deepseek/deepseek-chat-v3-0324 \
  -T max_turns=1 \
  -T judge_model=openrouter/deepseek/deepseek-chat-v3-0324
```

View results:

```bash
uv run inspect view
```

## Common Issues

### "No module named 'social_engineering_eval'"
The package isn't importable. Either:
1. Use `PYTHONPATH=. uv run inspect eval ...`
2. Or install with `uv pip install -e .`

### "No module named 'social_engineering_eval.task'" (with relative import error)
Relative imports were used. Change to absolute imports.

### "Multiple top-level packages discovered"
The `data/` directory is being picked up. Ensure `pyproject.toml` has the `[tool.setuptools.packages.find]` section.

### "OPENAI_API_KEY not defined"
The judge model defaults to OpenAI. Pass `-T judge_model=<your-provider-model>`.

### Python version errors
Requires Python 3.10+. Use `uv venv --python 3.10` to create the environment.

## Adding a New Evaluation

### Step-by-Step Guide

1. **Create directory**: `mkdir my_new_eval`

2. **Create the minimum required files**:
   - `__init__.py` - exports the task
   - `task.py` - defines the `@task` entry point

3. **Update `pyproject.toml`** to include the new package:
   ```toml
   [tool.setuptools.packages.find]
   include = ["phishing_eval*", "my_new_eval*"]
   ```

4. **Reinstall**: `uv pip install -e .`

### Minimal Task Example

```python
# my_new_eval/task.py
from inspect_ai import Task, task
from inspect_ai.dataset import Sample, Dataset
from inspect_ai.scorer import model_graded_qa
from inspect_ai.solver import generate

@task
def my_new_eval() -> Task:
    # Inline dataset for simplicity
    dataset = Dataset(samples=[
        Sample(input="What is 2+2?", target="4"),
        Sample(input="What is the capital of France?", target="Paris"),
    ])

    return Task(
        dataset=dataset,
        solver=generate(),  # Simple single-turn generation
        scorer=model_graded_qa(),  # Built-in LLM judge
    )
```

```python
# my_new_eval/__init__.py
from my_new_eval.task import my_new_eval
__all__ = ["my_new_eval"]
```

### Custom Solver Pattern

For multi-turn or complex logic:

```python
# my_new_eval/solver.py
from inspect_ai.solver import Solver, TaskState, Generate, solver

@solver
def my_custom_solver(some_param: str) -> Solver:
    async def solve(state: TaskState, generate: Generate) -> TaskState:
        # Your custom logic here
        # Access input: state.input_text
        # Access metadata: state.metadata.get("key")
        # Store results: state.metadata["result"] = value

        # Use the generate function for model calls
        response = await generate(state)

        return state

    return solve
```

### Custom Scorer Pattern

For custom evaluation logic:

```python
# my_new_eval/scorer.py
from inspect_ai.scorer import Score, Scorer, Target, scorer, metric

@scorer(metrics=[my_custom_metric()])
def my_custom_scorer() -> Scorer:
    async def score(state, target: Target) -> Score:
        # Access solver results from state.metadata
        result = state.metadata.get("result")

        # Compute score
        value = 1.0 if result == target.text else 0.0

        return Score(
            value=value,
            explanation="Why this score was given",
        )

    return score
```

### Custom Metric Pattern

```python
# my_new_eval/metrics.py
from inspect_ai.scorer import Metric, SampleScore, metric

@metric
def my_custom_metric() -> Metric:
    def compute(scores: list[SampleScore]) -> float:
        values = [s.score.value for s in scores if s.score.value is not None]
        return sum(values) / len(values) if values else 0.0

    return compute
```

### Checklist for New Evals

- [ ] Created directory with `__init__.py` and `task.py`
- [ ] Used **absolute imports** everywhere
- [ ] Added package to `pyproject.toml` include list
- [ ] Task function has `@task` decorator
- [ ] Task function returns a `Task` object
- [ ] `__init__.py` exports the task function
- [ ] Reinstalled with `uv pip install -e .`
- [ ] Tested with `uv run inspect eval my_new_eval/task.py --model <model>`

### Reusing Components

You can import from existing evals:

```python
# Reuse the social engineering scorer's metrics
from social_engineering_eval.metrics import avg_overall, avg_believability

# Reuse prompt patterns
from social_engineering_eval.prompts import format_conversation
```

### Data Loading Options

```python
# From JSON file
from inspect_ai.dataset import json_dataset
dataset = json_dataset("path/to/data.json", sample_fields=FieldSpec(...))

# From CSV
from inspect_ai.dataset import csv_dataset
dataset = csv_dataset("path/to/data.csv")

# From HuggingFace
from inspect_ai.dataset import hf_dataset
dataset = hf_dataset("dataset_name", split="test")

# Inline
from inspect_ai.dataset import Dataset, Sample
dataset = Dataset(samples=[Sample(input="...", target="...")])
```

## Documentation Guide

### Must-Read Docs by Component

Before writing code for a specific component, read these docs:

| Component | Must-Read Documentation |
|-----------|------------------------|
| **Tasks** | [Tutorial](https://inspect.aisi.org.uk/tutorial.html) - Start here for basics |
| **Datasets** | [Datasets](https://inspect.aisi.org.uk/datasets.html) - Loading, filtering, Sample fields |
| **Solvers** | [Solvers](https://inspect.aisi.org.uk/solvers.html) - Built-in solvers, chaining, custom solvers |
| **Scorers** | [Scorers](https://inspect.aisi.org.uk/scorers.html) - Built-in scorers, model-graded, custom scorers |
| **Agents** | [Agents](https://inspect.aisi.org.uk/agents.html) - Multi-turn, tool use, agent loops |
| **Multi-Agent** | [Multi-Agent](https://inspect.aisi.org.uk/multi-agent.html) - Handoffs, orchestration |
| **Tools** | [Tools](https://inspect.aisi.org.uk/tools.html) - Defining tools for agents |
| **Models** | [Models](https://inspect.aisi.org.uk/models.html) - Provider setup, model strings |
| **Model Providers** | [Providers](https://inspect.aisi.org.uk/providers.html) - OpenRouter, API keys, config |

### Key Documentation Pages

**Getting Started:**
- [Tutorial](https://inspect.aisi.org.uk/tutorial.html) - Basic eval structure
- [Workflow](https://inspect.aisi.org.uk/workflow.html) - Development workflow, debugging

**Core Concepts:**
- [Eval Logs](https://inspect.aisi.org.uk/eval-logs.html) - Understanding output logs
- [Eval Sets](https://inspect.aisi.org.uk/eval-sets.html) - Running multiple evals

**Advanced:**
- [Custom Agents](https://inspect.aisi.org.uk/agent-custom.html) - Building custom agent loops
- [Caching](https://inspect.aisi.org.uk/caching.html) - Caching API calls for development

### Where to Find Examples

**Official Examples Repository:**
```
https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals
```

| Example Eval | Good For Learning |
|--------------|-------------------|
| `agentharm/` | LLM-as-judge, custom scorers, adversarial evals, tool-based agents |
| `gdm_capabilities/` | Multi-step agent tasks |
| `gaia/` | Complex multi-modal agent evals |
| `mmlu/` | Simple multiple-choice scoring |
| `gpqa/` | Question-answering with chain-of-thought |
| `humaneval/` | Code generation and execution |
| `swe_bench/` | Complex coding tasks with sandboxed execution |

**To browse an example:**
```
https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/<eval_name>
```

### Reading Order for New Developers

1. **[Tutorial](https://inspect.aisi.org.uk/tutorial.html)** - Understand Task/Dataset/Solver/Scorer basics
2. **[Solvers](https://inspect.aisi.org.uk/solvers.html)** - Learn about `generate()`, chaining, custom solvers
3. **[Scorers](https://inspect.aisi.org.uk/scorers.html)** - Learn about `model_graded_qa()`, custom scorers
4. **Browse `agentharm/`** - See a real-world adversarial eval implementation
5. **[Agents](https://inspect.aisi.org.uk/agents.html)** - Only if you need multi-turn tool-using agents

### API Reference Locations

The docs don't have a traditional API reference, but each page has code examples. Key imports:

```python
# Core
from inspect_ai import Task, task

# Datasets
from inspect_ai.dataset import Dataset, Sample, json_dataset, csv_dataset, hf_dataset, FieldSpec

# Solvers
from inspect_ai.solver import Solver, TaskState, Generate, solver, generate, chain, system_message

# Scorers
from inspect_ai.scorer import Score, Scorer, Target, scorer, metric, model_graded_qa, model_graded_fact

# Models
from inspect_ai.model import get_model, ChatMessageSystem, ChatMessageUser, ChatMessageAssistant, GenerateConfig
```

### Useful CLI Commands

```bash
# List available tasks in a file
inspect list social_engineering_eval/task.py

# Run with debug logging
inspect eval social_engineering_eval/task.py --model <model> --log-level debug

# Limit to N samples
inspect eval social_engineering_eval/task.py --model <model> --limit 2

# View logs interactively
inspect view

# List recent logs
inspect log list

# Read a specific log
inspect log read logs/<file>.eval
```

## References

- [Inspect AI Docs](https://inspect.aisi.org.uk/)
- [Inspect Evals Repo](https://github.com/UKGovernmentBEIS/inspect_evals) - see `agentharm` for similar patterns
