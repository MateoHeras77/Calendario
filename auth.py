"""User authentication helpers using Supabase."""

from typing import Any, Dict

# Placeholder for a Supabase client
_supabase_client = None


def login_user() -> Dict[str, Any]:
    """Authenticate a user via Supabase.

    Returns a dictionary with user information on success.
    """
    raise NotImplementedError("login_user needs Supabase integration")


def fetch_user_data() -> Dict[str, Any]:
    """Return the authenticated user's data."""
    raise NotImplementedError("fetch_user_data needs Supabase integration")


def logout_user() -> None:
    """Log out the current user."""
    raise NotImplementedError("logout_user needs Supabase integration")
