"""
Sidebar rendering with API key input and progress tracking
"""
import streamlit as st
from utils.form_validation import FormValidator

def render_sidebar():
    """Render settings and progress in the main area (Alwrity Style)"""
    
    # 1. API Configuration Expander at the top
    with st.expander("API Configuration 🔑", expanded=not st.session_state.get('gemini_api_key')):
        api_key = st.text_input(
            "Enter your Gemini API Key",
            value=st.session_state.get('gemini_api_key', ''),
            type="password",
            help="Get your key from Google AI Studio",
            placeholder="AIza..."
        )
        if api_key != st.session_state.get('gemini_api_key'):
            st.session_state['gemini_api_key'] = api_key
            st.rerun()

    # 2. Progress Steps (Alwrity Style)
    with st.expander("PRO-TIP - Follow the steps below for best results. 💡", expanded=True):
        steps = [
            ("Company Overview", "🏢"),
            ("Marketing Details", "📢"),
            ("Competitor Info", "⚔️"),
            ("Financial Overview", "💰"),
            ("Generate Plan", "🚀")
        ]
        
        # Display progress as a horizontal row of status cards
        cols = st.columns(len(steps))
        for i, ((name, icon), col) in enumerate(zip(steps, cols), 1):
            if i < st.session_state.current_step:
                col.success(f"✅ {name}")
            elif i == st.session_state.current_step:
                col.info(f"{icon} **{name}**")
            else:
                col.write(f"⏳ {name}")
    
    # 3. Form Summary (if any data is present)
    if st.session_state.form_data.get('company_name'):
        with st.expander("Current Plan Summary 📄", expanded=False):
            st.write(f"**Company:** {st.session_state.form_data.get('company_name')}")
            validator = FormValidator()
            is_valid, _ = validator.validate_all_sections(st.session_state.form_data)
            if is_valid:
                st.success("All sections ready!")
            else:
                st.warning("Some sections still need details.")

    st.markdown("---")
