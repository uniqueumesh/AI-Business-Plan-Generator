"""
Marketing details form section
"""
import streamlit as st

def render_marketing_details():
    """Render the marketing details form section"""
    st.header("📈 Marketing Details")
    st.markdown("How will you attract and retain customers?")
    
    marketing_strategy = st.text_area(
        "Marketing Strategy *",
        value=st.session_state.form_data.get('marketing_strategy', ''),
        help="Describe your overall marketing approach and strategy",
        placeholder="Content marketing, influencer partnerships, and targeted social ads",
        height=120
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        customer_acquisition = st.text_area(
            "Customer Acquisition Methods",
            value=st.session_state.form_data.get('customer_acquisition', ''),
            help="How will you acquire new customers?",
            placeholder="Free 7‑day trial, referral program, email onboarding sequence",
            height=100
        )
        
        marketing_channels = st.text_area(
            "Marketing Channels",
            value=st.session_state.form_data.get('marketing_channels', ''),
            help="Which channels will you use for marketing?",
            placeholder="Instagram, YouTube, TikTok, and newsletter collaborations",
            height=100
        )
    
    with col2:
        budget_considerations = st.text_area(
            "Budget Considerations",
            value=st.session_state.form_data.get('budget_considerations', ''),
            help="What's your marketing budget and how will you allocate it?",
            placeholder="$2,000/month for ads, $500/month for content production",
            height=100
        )
    
    # Save form data
    st.session_state.form_data.update({
        'marketing_strategy': marketing_strategy,
        'customer_acquisition': customer_acquisition,
        'marketing_channels': marketing_channels,
        'budget_considerations': budget_considerations
    })
    
    return marketing_strategy, customer_acquisition, marketing_channels, budget_considerations
