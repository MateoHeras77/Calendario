"""Main entry point for the Streamlit application."""

import streamlit as st


def set_page_config():
    """Configure Streamlit page settings."""
    st.set_page_config(page_title="Calendario", page_icon="📅", layout="wide")


def main():
    """Launch the Streamlit app."""
    set_page_config()
    st.write("# Calendario de Turnos")
    # Navigation between views would be implemented here


if __name__ == "__main__":
    main()
