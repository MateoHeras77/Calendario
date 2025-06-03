"""View for displaying user shifts and marketplace shifts."""

from typing import List, Dict

import streamlit as st
from db import _get_shifts


def get_user_shifts(user_id: str) -> List[Dict]:
    """Fetch shifts assigned to a user from session state."""
    return [s for s in _get_shifts() if s.get("user_id") == user_id]


def get_market_shifts() -> List[Dict]:
    """Fetch shifts available on the market."""
    market = st.session_state.get("market", {})
    return [{"shift_id": sid, "offered_by": uid} for sid, uid in market.items()]


def display_calendar(user_id: str) -> None:
    """Render the calendar UI in Streamlit."""
    st.subheader("Mis turnos")
    shifts = get_user_shifts(user_id)
    if shifts:
        st.table(shifts)
    else:
        st.write("No tienes turnos asignados.")
