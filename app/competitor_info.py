"""
Competitor information form section
"""
import streamlit as st

def render_competitor_info():
    """Render the competitor information form section"""
    st.header("🏆 Competitor Information")
    st.markdown("Who are your competitors and what makes you different?")
    
    competitor_overview = st.text_area(
        "Competitor Overview *",
        value=st.session_state.form_data.get('competitor_overview', ''),
        help="Describe your main competitors and the competitive landscape",
        placeholder="FitApp, HealthPro — both offer generic plans and limited coaching",
        height=120
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        competitive_advantages = st.text_area(
            "Competitive Advantages *",
            value=st.session_state.form_data.get('competitive_advantages', ''),
            help="What advantages do you have over competitors?",
            placeholder="Personalized plans, AI‑driven coaching, progress tracking dashboard",
            height=100
        )
        
        market_positioning = st.text_area(
            "Market Positioning",
            value=st.session_state.form_data.get('market_positioning', ''),
            help="How do you position yourself in the market?",
            placeholder="Premium yet affordable alternative focusing on accountability",
            height=100
        )
    
    with col2:
        unique_value_prop = st.text_area(
            "Unique Value Proposition",
            value=st.session_state.form_data.get('unique_value_prop', ''),
            help="What unique value do you provide to customers?",
            placeholder="Daily micro‑workouts tailored to schedule and equipment",
            height=100
        )
    
    # Save form data
    st.session_state.form_data.update({
        'competitor_overview': competitor_overview,
        'competitive_advantages': competitive_advantages,
        'market_positioning': market_positioning,
        'unique_value_prop': unique_value_prop
    })
    
    return competitor_overview, competitive_advantages, market_positioning, unique_value_prop
