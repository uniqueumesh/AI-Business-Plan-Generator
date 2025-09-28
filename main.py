"""
AI Business Plan Generator - Main Entry Point
"""
import streamlit as st
from config import APP_TITLE
from app.session import initialize_session_state
from app.header import render_header
from app.sidebar import render_sidebar
from app.company_overview import render_company_overview
from app.marketing_details import render_marketing_details
from app.competitor_info import render_competitor_info
from app.financial_overview import render_financial_overview
from app.generate_section import render_generate_section
from app.navigation import render_navigation_buttons

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Render header
    render_header()
    
    # Render sidebar
    render_sidebar()
    
    # Render current step
    if st.session_state.current_step == 1:
        render_company_overview()
    elif st.session_state.current_step == 2:
        render_marketing_details()
    elif st.session_state.current_step == 3:
        render_competitor_info()
    elif st.session_state.current_step == 4:
        render_financial_overview()
    elif st.session_state.current_step == 5:
        render_generate_section()
    
    # Render navigation buttons
    if st.session_state.current_step < 5:
        render_navigation_buttons()
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**AI Business Plan Generator** | Powered by Google Gemini AI | "
        "For support, please check the documentation or contact support."
    )

if __name__ == "__main__":
    main()

