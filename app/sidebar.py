"""
Sidebar rendering with API key input and progress tracking
"""
import streamlit as st
from utils.form_validation import FormValidator

def render_sidebar():
    """Render the sidebar with progress indicator"""
    # API Key input
    st.sidebar.title("API Settings")
    api_key = st.sidebar.text_input(
        "Gemini API Key",
        value=st.session_state.get('gemini_api_key', ''),
        type="password",
        help="Enter your Google Gemini API key (kept only in this session)",
        placeholder="AIza..."
    )
    if api_key != st.session_state.get('gemini_api_key'):
        st.session_state['gemini_api_key'] = api_key
    
    st.sidebar.markdown("---")
    st.sidebar.title("Progress")
    
    steps = [
        "Company Overview",
        "Marketing Details", 
        "Competitor Information",
        "Financial Overview",
        "Generate Plan"
    ]
    
    for i, step in enumerate(steps, 1):
        if i < st.session_state.current_step:
            st.sidebar.success(f"✅ {step}")
        elif i == st.session_state.current_step:
            st.sidebar.info(f"🔄 {step}")
        else:
            st.sidebar.write(f"⏳ {step}")
    
    st.sidebar.markdown("---")
    
    # Show form data summary
    if st.session_state.form_data:
        st.sidebar.subheader("Form Summary")
        company_name = st.session_state.form_data.get('company_name', 'Not specified')
        st.sidebar.write(f"**Company:** {company_name}")
        
        # Show completion status
        validator = FormValidator()
        is_valid, errors = validator.validate_all_sections(st.session_state.form_data)
        if is_valid:
            st.sidebar.success("✅ All sections complete")
        else:
            st.sidebar.warning(f"⚠️ {len(errors)} sections need attention")
