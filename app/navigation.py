"""
Navigation buttons for form steps
"""
import streamlit as st
from utils.form_validation import FormValidator

def render_navigation_buttons():
    """Render navigation buttons"""
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.session_state.current_step > 1:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_step -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_step < 5:
            if st.button("Next ➡️", use_container_width=True, type="primary"):
                # Validate current step before proceeding
                validator = FormValidator()
                step_names = ['company_overview', 'marketing_details', 'competitor_info', 'financial_overview']
                current_step_name = step_names[st.session_state.current_step - 1]
                
                is_valid, errors = validator.validate_section(current_step_name, st.session_state.form_data)
                
                if is_valid:
                    st.session_state.current_step += 1
                    st.rerun()
                else:
                    st.error("Please complete all required fields before proceeding.")
                    st.markdown(validator.get_validation_message({current_step_name: errors}))
