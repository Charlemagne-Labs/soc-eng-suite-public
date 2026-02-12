"""Utility functions for data loading and helpers."""

import json
from pathlib import Path

from inspect_ai.dataset import Dataset, Sample, FieldSpec, json_dataset


def load_social_engineering_dataset(data_path: str | Path | None = None) -> Dataset:
    """Load social engineering challenges from JSON file.

    Args:
        data_path: Path to JSON file. Defaults to data/phishing_challenges.json

    Returns:
        Dataset of social engineering challenge samples
    """
    if data_path is None:
        # Default to data directory relative to this module
        data_path = Path(__file__).parent.parent / "data" / "generated_dataset.json"
    else:
        # Resolve relative paths from the project root, not the module directory
        data_path = Path(data_path)
        if not data_path.is_absolute():
            data_path = Path(__file__).parent.parent / data_path

    return json_dataset(
        str(data_path),
        sample_fields=FieldSpec(
            id="id",
            input="goal",  # The goal becomes the input prompt
            metadata=["target_profile", "platform", "goal", "_target", "_scam", "_action", "pretext", "psychological_levers"],
        ),
    )


def record_to_sample(record: dict) -> Sample:
    """Convert a raw JSON record to an Inspect Sample.

    This is an alternative way to load data if you need custom processing.

    Args:
        record: Dictionary with target_profile, goal, platform fields

    Returns:
        Inspect Sample object
    """
    return Sample(
        id=record.get("id", ""),
        input=record["goal"],
        metadata={
            "target_profile": record["target_profile"],
            "goal": record["goal"],
            "platform": record["platform"],
        },
    )


def load_social_engineering_dataset_manual(data_path: str | Path) -> Dataset:
    """Load social engineering challenges with manual parsing.

    Use this if you need more control over the loading process.

    Args:
        data_path: Path to JSON file

    Returns:
        Dataset of social engineering challenge samples
    """
    with open(data_path, "r") as f:
        records = json.load(f)

    samples = [record_to_sample(record) for record in records]
    return Dataset(samples=samples)
