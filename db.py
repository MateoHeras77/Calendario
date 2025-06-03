"""Database interaction layer using Supabase."""

from typing import Dict, Any

# Placeholder for a Supabase client
_supabase_client = None


def insert_shift(data: Dict[str, Any]) -> Dict[str, Any]:
    """Insert a new shift record into the database."""
    raise NotImplementedError("DB insert not implemented")


def update_shift(shift_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing shift record."""
    raise NotImplementedError("DB update not implemented")


def delete_shift(shift_id: str) -> None:
    """Delete a shift from the database."""
    raise NotImplementedError("DB delete not implemented")


def log_shift_change(action: str, data: Dict[str, Any]) -> None:
    """Record a change to a shift in the history table."""
    raise NotImplementedError("DB logging not implemented")
