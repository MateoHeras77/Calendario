"""Helpers for managing the shift marketplace."""

from typing import Dict

import streamlit as st
from db import _get_shifts


def _get_market() -> Dict[str, str]:
    """Return the marketplace mapping from session state."""
    return st.session_state.setdefault("market", {})


def offer_shift(user_id: str, shift_id: str) -> Dict:
    """Mark a user's shift as available in the market."""
    _get_market()[shift_id] = user_id
    return {"shift_id": shift_id, "offered_by": user_id}


def take_shift(user_id: str, shift_id: str) -> Dict:
    """Request to take an offered shift."""
    market = _get_market()
    if shift_id not in market:
        return {"error": "Shift not available"}
    st.session_state.setdefault("requests", {})[shift_id] = user_id
    return {"shift_id": shift_id, "requested_by": user_id}


def confirm_shift_transfer(from_user_id: str, to_user_id: str, shift_id: str) -> Dict:
    """Confirm a shift transfer between users."""
    market = _get_market()
    if market.get(shift_id) != from_user_id:
        return {"error": "Transfer not valid"}

    del market[shift_id]
    requests = st.session_state.setdefault("requests", {})
    requests.pop(shift_id, None)

    # update shift owner
    for shift in _get_shifts():
        if shift.get("id") == shift_id:
            shift["user_id"] = to_user_id
            break

    return {"shift_id": shift_id, "from": from_user_id, "to": to_user_id}
