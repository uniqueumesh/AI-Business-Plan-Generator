"""
Application header rendering
"""
import streamlit as st
from config import APP_DESCRIPTION

def render_header():
    """Render the application header"""
    st.title("📊 AI Business Plan Generator")
    st.markdown(f"*{APP_DESCRIPTION}*")
    st.markdown("---")
