"""
Sidebar rendering with API key input and progress tracking
"""
import streamlit as st
from utils.form_validation import FormValidator

def render_sidebar():
    """Render settings and progress in the main area (Alwrity Style)"""
    
    # 1. API Configuration Expander at the top
    from config import GEMINI_API_KEY
    
    # We use the backend key if available, but don't show it in the input box
    has_backend_key = bool(GEMINI_API_KEY)
    has_custom_key = bool(st.session_state.get('custom_api_key'))
    
    expander_label = "API Configuration 🔑"
    if not (has_backend_key or has_custom_key):
        expander_label += " (Action Required)"

    with st.expander(expander_label, expanded=not (has_backend_key or has_custom_key)):
        if has_backend_key and not has_custom_key:
            st.success("✅ A default API key is active. You can provide your own below to override it.")
        elif has_custom_key:
            st.info("💡 Using your custom API key.")
        else:
            st.warning("⚠️ No API key found. Please enter your own to continue.")

        custom_key = st.text_input(
            "Custom Gemini API Key",
            value=st.session_state.get('custom_api_key', ''),
            type="password",
            help="Your key is only kept for this session and will disappear when you close the tool.",
            placeholder="AIza..."
        )
        if custom_key != st.session_state.get('custom_api_key'):
            st.session_state['custom_api_key'] = custom_key
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
