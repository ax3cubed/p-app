import streamlit as st

def render_uploader():
    """Render the file uploader component."""
    return st.file_uploader("Upload Task Data (JSON)", type="json")
