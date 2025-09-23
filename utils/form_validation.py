"""
Form validation utilities for the AI Business Plan Generator
"""
from typing import Dict, Any, List, Tuple
from config import REQUIRED_FIELDS, ERROR_MESSAGES

class FormValidator:
    """Handles form validation for business plan generation"""
    
    def __init__(self):
        self.required_fields = REQUIRED_FIELDS
    
    def validate_section(self, section_name: str, form_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate a specific section of the form
        
        Args:
            section_name: Name of the section to validate
            form_data: Dictionary containing form data
            
        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []
        
        if section_name not in self.required_fields:
            return True, errors
        
        required_fields = self.required_fields[section_name]
        
        for field in required_fields:
            value = form_data.get(field, "").strip()
            if not value:
                errors.append(f"{field.replace('_', ' ').title()} is required")
        
        return len(errors) == 0, errors
    
    def validate_all_sections(self, form_data: Dict[str, Any]) -> Tuple[bool, Dict[str, List[str]]]:
        """
        Validate all sections of the form
        
        Args:
            form_data: Dictionary containing all form data
            
        Returns:
            Tuple of (is_valid, dict_of_section_errors)
        """
        all_errors = {}
        is_valid = True
        
        for section in self.required_fields.keys():
            section_valid, section_errors = self.validate_section(section, form_data)
            if not section_valid:
                all_errors[section] = section_errors
                is_valid = False
        
        return is_valid, all_errors
    
    def get_validation_message(self, section_errors: Dict[str, List[str]]) -> str:
        """
        Generate a user-friendly validation message
        
        Args:
            section_errors: Dictionary of section errors
            
        Returns:
            Formatted validation message
        """
        if not section_errors:
            return ""
        
        message = "Please complete the following required fields:\n\n"
        
        for section, errors in section_errors.items():
            section_name = section.replace('_', ' ').title()
            message += f"**{section_name}:**\n"
            for error in errors:
                message += f"• {error}\n"
            message += "\n"
        
        return message
    
    def check_field_length(self, field_value: str, min_length: int = 10, max_length: int = 5000) -> bool:
        """
        Check if a field value meets length requirements
        
        Args:
            field_value: The field value to check
            min_length: Minimum required length
            max_length: Maximum allowed length
            
        Returns:
            True if length is valid, False otherwise
        """
        if not field_value:
            return False
        
        length = len(field_value.strip())
        return min_length <= length <= max_length

