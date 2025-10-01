"""
Configuration settings for the AI Business Plan Generator
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"
MAX_RETRIES = 3
REQUEST_TIMEOUT = 60

# Application Configuration
APP_TITLE = "AI Business Plan Generator"
APP_DESCRIPTION = "Generate comprehensive business plans with AI assistance"

# Form Configuration
REQUIRED_FIELDS = {
    "company_overview": ["company_name", "business_description", "mission", "target_market"],
    "marketing_details": ["marketing_strategy"],
    "competitor_info": ["competitor_overview", "competitive_advantages"],
    "financial_overview": ["expected_costs", "financial_strategy", "projected_sales"]
}

# AI Prompt Templates
BUSINESS_PLAN_PROMPT = """
You are an expert business consultant. Generate a comprehensive business plan based on the following information:

COMPANY OVERVIEW:
- Company Name: {company_name}
- Business Description: {business_description}
- Mission Statement: {mission}
- Target Market: {target_market}

MARKETING DETAILS:
- Marketing Strategy: {marketing_strategy}
- Customer Acquisition: {customer_acquisition}
- Marketing Channels: {marketing_channels}
- Budget Considerations: {budget_considerations}

COMPETITOR INFORMATION:
- Competitor Overview: {competitor_overview}
- Competitive Advantages: {competitive_advantages}
- Market Positioning: {market_positioning}
- Unique Value Proposition: {unique_value_prop}

FINANCIAL OVERVIEW:
- Expected Costs: {expected_costs}
- Financial Strategy: {financial_strategy}
- Projected Sales: {projected_sales}
- Revenue Model: {revenue_model}
- Funding Requirements: {funding_requirements}

Please generate a professional business plan with the following structure:
1. Executive Summary
2. Company Description
3. Market Analysis
4. Organization & Management
5. Service or Product Line
6. Marketing & Sales Strategy
7. Financial Projections
8. Funding Request (if applicable)
9. Appendix

Make the plan detailed, professional, and actionable. Use clear headings and bullet points for easy reading.
"""

# Error Messages
ERROR_MESSAGES = {
    "api_key_missing": "Please set your GEMINI_API_KEY in the environment variables",
    "api_error": "There was an error generating your business plan. Please try again.",
    "validation_error": "Please fill in all required fields before generating the plan",
    "network_error": "Network error. Please check your connection and try again."
}
