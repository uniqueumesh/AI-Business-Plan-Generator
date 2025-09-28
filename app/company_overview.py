"""
Company overview form section
"""
import streamlit as st

def render_company_overview():
    """Render the company overview form section"""
    st.header("🏢 Company Overview")
    st.markdown("Tell us about your business and what makes it unique.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input(
            "Company Name *",
            value=st.session_state.form_data.get('company_name', ''),
            help="Enter your company or business name",
            placeholder="Acme Fitness Co"
        )
        
        target_market = st.text_area(
            "Target Market *",
            value=st.session_state.form_data.get('target_market', ''),
            help="Describe your ideal customers and target audience",
            placeholder="Professionals aged 25–45 in urban areas seeking convenient home workouts",
            height=100
        )
    
    with col2:
        business_description = st.text_area(
            "Business/Product Description *",
            value=st.session_state.form_data.get('business_description', ''),
            help="Describe what your business does or what product/service you offer",
            placeholder="A mobile app offering personalized workout plans and nutrition guidance",
            height=100
        )
        
        mission = st.text_area(
            "Mission Statement *",
            value=st.session_state.form_data.get('mission', ''),
            help="What is your company's mission and purpose?",
            placeholder="Empower busy professionals to stay healthy through simple daily routines",
            height=100
        )
    
    # Save form data
    st.session_state.form_data.update({
        'company_name': company_name,
        'business_description': business_description,
        'mission': mission,
        'target_market': target_market
    })
    
    return company_name, business_description, mission, target_market
