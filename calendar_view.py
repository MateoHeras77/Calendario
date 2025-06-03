"""View for displaying user shifts and marketplace shifts."""

from typing import List, Dict


def get_user_shifts(user_id: str) -> List[Dict]:
    """Fetch shifts assigned to a user."""
    raise NotImplementedError("Supabase query not implemented")


def get_market_shifts() -> List[Dict]:
    """Fetch shifts available on the market."""
    raise NotImplementedError("Supabase query not implemented")


def display_calendar(user_id: str) -> None:
    """Render the calendar UI in Streamlit."""
    raise NotImplementedError("Streamlit calendar display not implemented")
