"""
Session state management
"""
import streamlit as st

def initialize_session_state():
    """Initialize session state variables"""
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'business_plan_generated' not in st.session_state:
        st.session_state.business_plan_generated = False
