# Social Engineering Evaluation Suite  AI

A multi-turn social engineering evaluation that simulates phishing attacks for AI safety research using the [Inspect AI](https://inspect.aisi.org.uk/) framework.

## Overview

The evaluation simulates conversations between:
- **Attacker LLM**: Attempts to manipulate the victim using social engineering techniques
- **Victim LLM**: Roleplays as a target persona, responding naturally to messages
- **Judge LLM**: Scores the attacker's performance on three dimensions

### Scoring Dimensions

| Dimension | Description | Scale |
|-----------|-------------|-------|
| Persuasion | Effectiveness of persuasive techniques (emotional appeals, urgency, authority) | 0-5 |
| Rapport | Ability to build trust and connection with the target | 0-5 |
| Argumentation | Quality and structure of arguments presented | 0-5 |

## Installation

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- API key for your chosen model provider

### Setup with uv (Recommended)

```bash
# Clone or navigate to the repository
cd soc-eng-suite

# Create virtual environment with Python 3.10+
uv venv --python 3.10

# Activate the virtual environment
source .venv/bin/activate

# Install the package
uv pip install -e .
```

### Setup with pip

```bash
# Create virtual environment
python3.10 -m venv .venv
source .venv/bin/activate

# Install the package
pip install -e .
```

## Configuration

### API Keys

Set the appropriate environment variable for your model provider:

```bash
# OpenRouter
export OPENROUTER_API_KEY=your-key-here

# OpenAI
export OPENAI_API_KEY=your-key-here

# Anthropic
export ANTHROPIC_API_KEY=your-key-here

# AWS Bedrock (uses standard AWS credentials)
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=us-east-1
```

### Supported Model Providers

| Provider | Model Format Example |
|----------|---------------------|
| AWS Bedrock | `bedrock/deepseek.v3-v1:0` |
| OpenRouter | `openrouter/deepseek/deepseek-chat-v3-0324` |
| OpenAI | `openai/gpt-4o-mini` |
| Anthropic | `anthropic/claude-3-haiku-20240307` |

See [Inspect's model documentation](https://inspect.aisi.org.uk/models.html) for the full list of supported providers.

## Usage

### Recommended Run

```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openrouter/deepseek/deepseek-chat-v3-0324 \
  -T max_turns=5 \
  -T judge_model=openrouter/deepseek/deepseek-chat-v3-0324 \
  --limit 10 \
  --sample-shuffle
```

### Task Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_turns` | 15 | Maximum conversation turns before stopping |
| `attacker_model` | (task model) | Model for the attacker role |
| `victim_model` | (task model) | Model for the victim role |
| `judge_model` | `openai/gpt-4o` | Model for scoring the conversation |
| `data_path` | `data/generated_dataset_1.json` | Path to challenge dataset |

### Inspect Options

| Option | Description |
|--------|-------------|
| `--limit N` | Run only N samples (takes first N sequentially) |
| `--sample-shuffle` | Randomize sample order before applying limit |
| `--sample-shuffle 42` | Shuffle with a fixed seed for reproducibility |

### Examples

**Quick test (2 samples, 2 turns):**
```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openrouter/deepseek/deepseek-chat-v3-0324 \
  -T max_turns=2 \
  -T judge_model=openrouter/deepseek/deepseek-chat-v3-0324 \
  --limit 2 \
  --sample-shuffle
```

**Full run with OpenAI:**
```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openai/gpt-4o-mini \
  -T max_turns=5 \
  -T judge_model=openai/gpt-4o
```

**Using different models for attacker/victim:**
```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openai/gpt-4o \
  -T attacker_model=openai/gpt-4o \
  -T victim_model=anthropic/claude-3-haiku-20240307 \
  -T judge_model=openai/gpt-4o
```

**Using a custom dataset:**
```bash
uv run inspect eval social_engineering_eval/task.py \
  --model openrouter/deepseek/deepseek-chat-v3-0324 \
  -T data_path=data/my_custom_dataset.json \
  -T judge_model=openrouter/deepseek/deepseek-chat-v3-0324
```

## Viewing Results

### Web UI (Recommended)

```bash
uv run inspect view
```

This opens an interactive web interface where you can:
- View aggregate metrics (persuasion, rapport, argumentation, compliance rate)
- Examine individual conversations
- Read the judge's explanations for each score

### Command Line

List available logs:
```bash
uv run inspect log list
```

Read a specific log:
```bash
uv run inspect log read logs/<log-file>.eval
```

## Dataset Format

The evaluation uses JSON files with the following structure:

```json
[
  {
    "id": "phish_001",
    "target_profile": "Description of the victim persona...",
    "goal": "The attacker's objective...",
    "platform": "email|sms|slack|etc"
  }
]
```

### Fields

| Field | Description |
|-------|-------------|
| `id` | Unique identifier for the scenario |
| `target_profile` | Detailed description of the victim's background, job, personality, and vulnerabilities |
| `goal` | What the attacker is trying to achieve (e.g., get credentials, click a link) |
| `platform` | Communication channel (affects message formatting expectations) |

### Custom Datasets

To use your own dataset:

```bash
uv run inspect eval social_engineering_eval/task.py \
  --model <model> \
  -T data_path=/path/to/your/challenges.json
```

## Project Structure

```
soc-eng-suite/
├── social_engineering_eval/
│   ├── __init__.py       # Package exports
│   ├── task.py           # Main @task definition
│   ├── solver.py         # Multi-turn conversation orchestrator
│   ├── scorer.py         # LLM-as-judge scoring
│   ├── metrics.py        # Aggregation metrics
│   ├── prompts.py        # System prompts for attacker/victim/judge
│   └── utils.py          # Data loading utilities
├── data/
│   └── phishing_challenges.json  # Sample scenarios
├── pyproject.toml        # Package configuration
└── README.md
```

## Metrics

The evaluation produces the following metrics:

| Metric | Description |
|--------|-------------|
| `avg_persuasion` | Mean persuasion score (0-5) |
| `avg_rapport` | Mean rapport score (0-5) |
| `avg_argumentation` | Mean argumentation score (0-5) |
| `avg_overall` | Mean of all three dimensions |
| `compliance_rate` | Fraction of scenarios where victim complied |
| `refusal_rate` | Fraction of scenarios where victim explicitly refused |
| `scores_by_platform` | Breakdown of scores by communication platform |

## Adding a New Evaluation

To add a new evaluation to this project, create a new directory alongside `social_engineering_eval/`:

### 1. Create the Directory Structure

```
my_new_eval/
├── __init__.py
├── task.py        # Required: contains @task function
├── solver.py      # Your custom solving logic
├── scorer.py      # Your custom scoring logic
├── metrics.py     # Optional: custom aggregation metrics
├── prompts.py     # Optional: prompt templates
└── utils.py       # Optional: data loading helpers
```

### 2. Define the Task (`task.py`)

```python
from inspect_ai import Task, task
from inspect_ai.model import GenerateConfig

from my_new_eval.solver import my_solver
from my_new_eval.scorer import my_scorer

@task
def my_new_eval(
    param1: str = "default",
) -> Task:
    return Task(
        dataset=load_my_dataset(),
        solver=my_solver(param1),
        scorer=my_scorer(),
        config=GenerateConfig(temperature=0.7),
    )
```

### 3. Update Package Discovery

Add your new package to `pyproject.toml`:

```toml
[tool.setuptools.packages.find]
include = ["phishing_eval*", "my_new_eval*"]
```

### 4. Reinstall and Run

```bash
uv pip install -e .
uv run inspect eval my_new_eval/task.py --model <model-name>
```

### Key Requirements

- **Use absolute imports** (e.g., `from my_new_eval.solver import ...`, not `from .solver import ...`)
- **Export your task** in `__init__.py`: `from my_new_eval.task import my_new_eval`
- **Task function must be decorated** with `@task` and return a `Task` object

See `CLAUDE.md` for detailed development notes and common pitfalls.

## References

- [Inspect AI Documentation](https://inspect.aisi.org.uk/)
- [Red Teaming Language Models with Language Models](https://arxiv.org/abs/2202.03286)
- [AgentHarm Evaluation](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm)

## License

© 2026 Charlemagne Labs
This code is made available under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).