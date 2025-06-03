"""Database interaction layer using Supabase."""

from typing import Dict, Any, List

import streamlit as st


def _get_shifts() -> List[Dict[str, Any]]:
    """Return the list that stores shifts in session state."""
    return st.session_state.setdefault("shifts", [])


def insert_shift(data: Dict[str, Any]) -> Dict[str, Any]:
    """Insert a new shift record into the session state database."""
    _get_shifts().append(data)
    log_shift_change("insert", data)
    return data


def update_shift(shift_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing shift record."""
    for shift in _get_shifts():
        if shift.get("id") == shift_id:
            shift.update(data)
            log_shift_change("update", {"id": shift_id, **data})
            break
    return data


def delete_shift(shift_id: str) -> None:
    """Delete a shift from the session state database."""
    shifts = _get_shifts()
    st.session_state["shifts"] = [s for s in shifts if s.get("id") != shift_id]
    log_shift_change("delete", {"id": shift_id})


def log_shift_change(action: str, data: Dict[str, Any]) -> None:
    """Record a change to a shift in the history list."""
    history = st.session_state.setdefault("history", [])
    history.append({"action": action, **data})
