"""
AI Business Plan Generator - Main Streamlit Application
"""
import streamlit as st
import time
from typing import Dict, Any
from utils.api_client import GeminiAPIClient
from utils.form_validation import FormValidator
from utils.business_plan_formatter import BusinessPlanFormatter
from config import APP_TITLE, APP_DESCRIPTION, ERROR_MESSAGES

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize session state variables"""
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'business_plan_generated' not in st.session_state:
        st.session_state.business_plan_generated = False

def render_header():
    """Render the application header"""
    st.title("📊 AI Business Plan Generator")
    st.markdown(f"*{APP_DESCRIPTION}*")
    st.markdown("---")

def render_sidebar():
    """Render the sidebar with progress indicator"""
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

def render_company_overview():
    """Render the company overview form section"""
    st.header("🏢 Company Overview")
    st.markdown("Tell us about your business and what makes it unique.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input(
            "Company Name *",
            value=st.session_state.form_data.get('company_name', ''),
            help="Enter your company or business name"
        )
        
        target_market = st.text_area(
            "Target Market *",
            value=st.session_state.form_data.get('target_market', ''),
            help="Describe your ideal customers and target audience",
            height=100
        )
    
    with col2:
        business_description = st.text_area(
            "Business/Product Description *",
            value=st.session_state.form_data.get('business_description', ''),
            help="Describe what your business does or what product/service you offer",
            height=100
        )
        
        mission = st.text_area(
            "Mission Statement *",
            value=st.session_state.form_data.get('mission', ''),
            help="What is your company's mission and purpose?",
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

def render_marketing_details():
    """Render the marketing details form section"""
    st.header("📈 Marketing Details")
    st.markdown("How will you attract and retain customers?")
    
    marketing_strategy = st.text_area(
        "Marketing Strategy *",
        value=st.session_state.form_data.get('marketing_strategy', ''),
        help="Describe your overall marketing approach and strategy",
        height=120
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        customer_acquisition = st.text_area(
            "Customer Acquisition Methods",
            value=st.session_state.form_data.get('customer_acquisition', ''),
            help="How will you acquire new customers?",
            height=100
        )
        
        marketing_channels = st.text_area(
            "Marketing Channels",
            value=st.session_state.form_data.get('marketing_channels', ''),
            help="Which channels will you use for marketing?",
            height=100
        )
    
    with col2:
        budget_considerations = st.text_area(
            "Budget Considerations",
            value=st.session_state.form_data.get('budget_considerations', ''),
            help="What's your marketing budget and how will you allocate it?",
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

def render_competitor_info():
    """Render the competitor information form section"""
    st.header("🏆 Competitor Information")
    st.markdown("Who are your competitors and what makes you different?")
    
    competitor_overview = st.text_area(
        "Competitor Overview *",
        value=st.session_state.form_data.get('competitor_overview', ''),
        help="Describe your main competitors and the competitive landscape",
        height=120
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        competitive_advantages = st.text_area(
            "Competitive Advantages *",
            value=st.session_state.form_data.get('competitive_advantages', ''),
            help="What advantages do you have over competitors?",
            height=100
        )
        
        market_positioning = st.text_area(
            "Market Positioning",
            value=st.session_state.form_data.get('market_positioning', ''),
            help="How do you position yourself in the market?",
            height=100
        )
    
    with col2:
        unique_value_prop = st.text_area(
            "Unique Value Proposition",
            value=st.session_state.form_data.get('unique_value_prop', ''),
            help="What unique value do you provide to customers?",
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
            height=100
        )
        
        financial_strategy = st.text_area(
            "Financial Strategy *",
            value=st.session_state.form_data.get('financial_strategy', ''),
            help="How will you manage your finances and cash flow?",
            height=100
        )
    
    with col2:
        projected_sales = st.text_area(
            "Projected Sales *",
            value=st.session_state.form_data.get('projected_sales', ''),
            help="What are your sales projections for the first year?",
            height=100
        )
        
        revenue_model = st.text_area(
            "Revenue Model",
            value=st.session_state.form_data.get('revenue_model', ''),
            help="How will you generate revenue?",
            height=100
        )
    
    funding_requirements = st.text_area(
        "Funding Requirements",
        value=st.session_state.form_data.get('funding_requirements', ''),
        help="Do you need funding? If so, how much and for what?",
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

def generate_business_plan():
    """Generate the business plan using AI"""
    try:
        # Initialize API client
        api_client = GeminiAPIClient()
        
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

def render_navigation_buttons():
    """Render navigation buttons"""
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.session_state.current_step > 1:
            if st.button("⬅️ Previous", use_container_width=True):
                st.session_state.current_step -= 1
                st.rerun()
    
    with col3:
        if st.session_state.current_step < 5:
            if st.button("Next ➡️", use_container_width=True, type="primary"):
                # Validate current step before proceeding
                validator = FormValidator()
                step_names = ['company_overview', 'marketing_details', 'competitor_info', 'financial_overview']
                current_step_name = step_names[st.session_state.current_step - 1]
                
                is_valid, errors = validator.validate_section(current_step_name, st.session_state.form_data)
                
                if is_valid:
                    st.session_state.current_step += 1
                    st.rerun()
                else:
                    st.error("Please complete all required fields before proceeding.")
                    st.markdown(validator.get_validation_message({current_step_name: errors}))

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
