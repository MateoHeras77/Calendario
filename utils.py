"""Utility functions used across the project."""

from datetime import datetime
from typing import Dict


def format_datetime(timestamp: float) -> str:
    """Return a formatted date-time string."""
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def validate_shift_data(data: Dict) -> bool:
    """Basic validation of shift dictionary structure."""
    required_keys = {"id", "start", "end", "type"}
    return required_keys.issubset(data.keys())


def get_shift_color(shift_type: str) -> str:
    """Return a color based on the shift type."""
    mapping = {
        "morning": "green",
        "evening": "orange",
        "night": "blue",
    }
    return mapping.get(shift_type, "gray")
