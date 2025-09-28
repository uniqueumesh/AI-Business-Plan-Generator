"""
Business plan generation logic
"""
import streamlit as st
import time
from utils.api_client import GeminiAPIClient
from utils.business_plan_formatter import BusinessPlanFormatter
from config import ERROR_MESSAGES

def generate_business_plan():
    """Generate the business plan using AI"""
    try:
        # Retrieve API key from session
        api_key = st.session_state.get('gemini_api_key', '')
        if not api_key:
            st.error("Please enter your Gemini API key in the sidebar to continue.")
            return
        # Initialize API client
        api_client = GeminiAPIClient(api_key=api_key)
        
        # Show progress
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🤖 Generating your business plan...")
        progress_bar.progress(25)
        
        # Generate business plan
        business_plan = api_client.generate_business_plan(st.session_state.form_data)
        
        progress_bar.progress(75)
        status_text.text("📝 Formatting your business plan...")
        
        if business_plan:
            # Display the business plan
            st.session_state.business_plan_generated = True
            progress_bar.progress(100)
            status_text.text("✅ Business plan generated successfully!")
            
            # Clear progress indicators
            time.sleep(1)
            progress_bar.empty()
            status_text.empty()
            
            # Display the plan
            formatter = BusinessPlanFormatter()
            formatter.display_business_plan(business_plan, st.session_state.form_data.get('company_name', 'Your Company'))
            
        else:
            st.error(ERROR_MESSAGES['api_error'])
            
    except Exception as e:
        st.error(f"Error generating business plan: {str(e)}")
        st.info("Please check your API key and try again.")
