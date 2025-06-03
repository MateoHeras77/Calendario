"""User authentication helpers using Supabase."""

from typing import Any, Dict, Optional

import streamlit as st


def login_user(username: str) -> Dict[str, Any]:
    """Authenticate a user and store their info in session state."""
    user_data = {"id": username, "username": username}
    st.session_state["user"] = user_data
    return user_data


def fetch_user_data() -> Optional[Dict[str, Any]]:
    """Return the authenticated user's data if available."""
    return st.session_state.get("user")


def logout_user() -> None:
    """Log out the current user and clear session data."""
    st.session_state.pop("user", None)
