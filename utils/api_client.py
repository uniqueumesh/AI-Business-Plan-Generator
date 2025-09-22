"""
Gemini API client for generating business plans
"""
import google.generativeai as genai
from typing import Dict, Any, Optional
import time
import streamlit as st
from config import GEMINI_API_KEY, GEMINI_MODEL, MAX_RETRIES, REQUEST_TIMEOUT, ERROR_MESSAGES

class GeminiAPIClient:
    """Client for interacting with Google Gemini API"""
    
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError(ERROR_MESSAGES["api_key_missing"])
        
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(GEMINI_MODEL)
    
    def generate_business_plan(self, form_data: Dict[str, Any]) -> str:
        """
        Generate a business plan using the provided form data
        
        Args:
            form_data: Dictionary containing all form inputs
            
        Returns:
            Generated business plan as string
        """
        try:
            # Prepare the prompt with form data
            prompt = self._prepare_prompt(form_data)
            
            # Generate content with retry logic
            for attempt in range(MAX_RETRIES):
                try:
                    response = self.model.generate_content(
                        prompt,
                        generation_config=genai.types.GenerationConfig(
                            temperature=0.7,
                            max_output_tokens=4000,
                        )
                    )
                    
                    if response.text:
                        return response.text
                    else:
                        raise Exception("Empty response from API")
                        
                except Exception as e:
                    if attempt == MAX_RETRIES - 1:
                        raise e
                    time.sleep(2 ** attempt)  # Exponential backoff
            
        except Exception as e:
            st.error(f"{ERROR_MESSAGES['api_error']}: {str(e)}")
            return None
    
    def _prepare_prompt(self, form_data: Dict[str, Any]) -> str:
        """Prepare the prompt with form data"""
        from config import BUSINESS_PLAN_PROMPT
        
        # Fill in the prompt template with form data
        prompt = BUSINESS_PLAN_PROMPT.format(
            company_name=form_data.get("company_name", ""),
            business_description=form_data.get("business_description", ""),
            mission=form_data.get("mission", ""),
            target_market=form_data.get("target_market", ""),
            marketing_strategy=form_data.get("marketing_strategy", ""),
            customer_acquisition=form_data.get("customer_acquisition", ""),
            marketing_channels=form_data.get("marketing_channels", ""),
            budget_considerations=form_data.get("budget_considerations", ""),
            competitor_overview=form_data.get("competitor_overview", ""),
            competitive_advantages=form_data.get("competitive_advantages", ""),
            market_positioning=form_data.get("market_positioning", ""),
            unique_value_prop=form_data.get("unique_value_prop", ""),
            expected_costs=form_data.get("expected_costs", ""),
            financial_strategy=form_data.get("financial_strategy", ""),
            projected_sales=form_data.get("projected_sales", ""),
            revenue_model=form_data.get("revenue_model", ""),
            funding_requirements=form_data.get("funding_requirements", "")
        )
        
        return prompt
