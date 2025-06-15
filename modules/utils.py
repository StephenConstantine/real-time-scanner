"""Utility functions for the Real-Time Event Exploration System.

This module provides common functionality used across all modules,
including prompt loading, file operations, and logging utilities.
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def load_prompt(prompt_name: str) -> str:
    """Load a specific prompt from the prompts.txt file.
    
    Args:
        prompt_name: The name of the prompt section to load
        
    Returns:
        The prompt text as a string
        
    Raises:
        FileNotFoundError: If prompts.txt doesn't exist
        ValueError: If the prompt section isn't found
    """
    prompts_file = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'prompts.txt')
    
    if not os.path.exists(prompts_file):
        raise FileNotFoundError(f"Prompts file not found: {prompts_file}")
    
    with open(prompts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the content to find the specific prompt
    sections = content.split('---')
    
    for section in sections:
        if f"### {prompt_name}" in section:
            # Extract the prompt text after the header
            lines = section.strip().split('\n')
            prompt_lines = []
            header_found = False
            
            for line in lines:
                if line.strip().startswith(f"### {prompt_name}"):
                    header_found = True
                    continue
                elif header_found:
                    prompt_lines.append(line)
            
            return '\n'.join(prompt_lines).strip()
    
    raise ValueError(f"Prompt section '{prompt_name}' not found in prompts.txt")


def save_result(data: Dict[Any, Any], step_name: str, event_name: str = "unknown") -> str:
    """Save step results to the results directory with standardized naming.
    
    Args:
        data: The data to save as JSON
        step_name: Name of the step (e.g., 'twitter_preview')
        event_name: Name of the event (sanitized for filename)
        
    Returns:
        The full path to the saved file
    """
    # Sanitize event name for filename
    safe_event_name = "".join(c for c in event_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_event_name = safe_event_name.replace(' ', '_')
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create filename
    filename = f"{step_name}_{safe_event_name}_{timestamp}.json"
    
    # Ensure results directory exists
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    # Save file
    filepath = os.path.join(results_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    logger.info(f"Results saved to: {filepath}")
    return filepath


def load_result(filepath: str) -> Dict[Any, Any]:
    """Load a previously saved result file.
    
    Args:
        filepath: Path to the JSON result file
        
    Returns:
        The loaded data as a dictionary
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Result file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    logger.info(f"Results loaded from: {filepath}")
    return data


def get_user_confirmation(message: str, default: bool = False) -> bool:
    """Get user confirmation with a yes/no prompt.
    
    Args:
        message: The message to display to the user
        default: Default value if user just presses Enter
        
    Returns:
        True if user confirms, False otherwise
    """
    default_text = "(Y/n)" if default else "(y/N)"
    response = input(f"{message} {default_text}: ").strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes', '1', 'true']


def sanitize_filename(filename: str) -> str:
    """Sanitize a string to be safe for use as a filename.
    
    Args:
        filename: The original filename string
        
    Returns:
        A sanitized filename string
    """
    # Remove or replace unsafe characters
    safe_chars = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_', '.'))
    # Replace spaces with underscores and remove extra whitespace
    return safe_chars.replace(' ', '_').strip()


def format_timestamp() -> str:
    """Generate a standardized timestamp string.
    
    Returns:
        Timestamp in YYYYMMDD_HHMMSS format
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S")

