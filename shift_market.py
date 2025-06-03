"""Helpers for managing the shift marketplace."""

from typing import Dict


def offer_shift(user_id: str, shift_id: str) -> Dict:
    """Mark a user's shift as available."""
    raise NotImplementedError("Supabase update not implemented")


def take_shift(user_id: str, shift_id: str) -> Dict:
    """Request to take an offered shift."""
    raise NotImplementedError("Supabase update not implemented")


def confirm_shift_transfer(from_user_id: str, to_user_id: str, shift_id: str) -> Dict:
    """Confirm a shift transfer between users."""
    raise NotImplementedError("Supabase update not implemented")
