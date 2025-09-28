"""
Business plan generation section
"""
import streamlit as st
from utils.form_validation import FormValidator
from utils.business_plan_formatter import BusinessPlanFormatter
from app.business_plan_generator import generate_business_plan

def render_generate_section():
    """Render the business plan generation section"""
    st.header("🚀 Generate Your Business Plan")
    
    # Show form summary
    formatter = BusinessPlanFormatter()
    summary = formatter.create_summary_card(st.session_state.form_data)
    st.markdown(summary)
    
    # Validation
    validator = FormValidator()
    is_valid, errors = validator.validate_all_sections(st.session_state.form_data)
    
    if not is_valid:
        st.error("Please complete all required fields before generating your business plan.")
        st.markdown(validator.get_validation_message(errors))
        return
    
    # Generate button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎯 Generate Business Plan", type="primary", use_container_width=True):
            generate_business_plan()
