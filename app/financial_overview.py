"""
Financial overview form section
"""
import streamlit as st

def render_financial_overview():
    """Render the financial overview form section"""
    st.header("💰 Financial Overview")
    st.markdown("What are your financial projections and strategy?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        expected_costs = st.text_area(
            "Expected Costs *",
            value=st.session_state.form_data.get('expected_costs', ''),
            help="What are your expected startup and operational costs?",
            placeholder="Development $8k, hosting $200/mo, marketing $2k/mo",
            height=100
        )
        
        financial_strategy = st.text_area(
            "Financial Strategy *",
            value=st.session_state.form_data.get('financial_strategy', ''),
            help="How will you manage your finances and cash flow?",
            placeholder="Keep CAC:LTV at 1:3, reinvest 30% of profits into growth",
            height=100
        )
    
    with col2:
        projected_sales = st.text_area(
            "Projected Sales *",
            value=st.session_state.form_data.get('projected_sales', ''),
            help="What are your sales projections for the first year?",
            placeholder="500 subscriptions in year 1 at $15/month",
            height=100
        )
        
        revenue_model = st.text_area(
            "Revenue Model",
            value=st.session_state.form_data.get('revenue_model', ''),
            help="How will you generate revenue?",
            placeholder="Monthly subscription with annual discount",
            height=100
        )
    
    funding_requirements = st.text_area(
        "Funding Requirements",
        value=st.session_state.form_data.get('funding_requirements', ''),
        help="Do you need funding? If so, how much and for what?",
        placeholder="$50k to cover 6 months runway and marketing tests",
        height=80
    )
    
    # Save form data
    st.session_state.form_data.update({
        'expected_costs': expected_costs,
        'financial_strategy': financial_strategy,
        'projected_sales': projected_sales,
        'revenue_model': revenue_model,
        'funding_requirements': funding_requirements
    })
    
    return expected_costs, financial_strategy, projected_sales, revenue_model, funding_requirements
