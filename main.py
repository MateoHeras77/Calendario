"""Main entry point for the Streamlit application."""

import streamlit as st

from auth import login_user, fetch_user_data, logout_user
from calendar_view import display_calendar
from shift_market import offer_shift, take_shift, _get_market


def set_page_config() -> None:
    """Configure Streamlit page settings."""
    st.set_page_config(page_title="Calendario", page_icon="📅", layout="wide")


def show_login() -> None:
    """Display a simple login form."""
    st.write("# Iniciar sesión")
    username = st.text_input("Usuario")
    if st.button("Entrar") and username:
        login_user(username)
        st.experimental_rerun()


def show_calendar(user: dict) -> None:
    """Show the user's calendar."""
    display_calendar(user["id"])


def show_shift_market(user: dict) -> None:
    """Interface to offer and take shifts."""
    st.subheader("Mercado de turnos")

    with st.form("offer_form"):
        st.write("Ofrecer turno")
        shift_id = st.text_input("ID del turno a ofrecer")
        if st.form_submit_button("Ofrecer") and shift_id:
            offer_shift(user["id"], shift_id)
            st.experimental_rerun()

    st.write("---")
    st.write("Turnos disponibles")
    market = _get_market()
    if market:
        st.table([
            {"shift_id": sid, "ofrecido_por": uid} for sid, uid in market.items()
        ])
    else:
        st.write("No hay turnos disponibles.")

    with st.form("take_form"):
        st.write("Tomar turno")
        take_id = st.text_input("ID del turno a tomar")
        if st.form_submit_button("Solicitar") and take_id:
            take_shift(user["id"], take_id)
            st.experimental_rerun()


def show_subscription() -> None:
    """Allow the user to store a subscription calendar link."""
    st.subheader("Suscripción de calendario")
    url = st.text_input(
        "Enlace de suscripción", value=st.session_state.get("subscription_url", "")
    )
    st.session_state["subscription_url"] = url


def main() -> None:
    """Launch the Streamlit app."""
    set_page_config()
    user = fetch_user_data()

    if not user:
        show_login()
        return

    st.sidebar.write(f"Hola, {user['username']}")
    if st.sidebar.button("Cerrar sesión"):
        logout_user()
        st.experimental_rerun()

    page = st.sidebar.radio(
        "Navegación", ["Calendario", "Mercado", "Suscripción"]
    )

    if page == "Calendario":
        show_calendar(user)
    elif page == "Mercado":
        show_shift_market(user)
    else:
        show_subscription()


if __name__ == "__main__":
    main()
