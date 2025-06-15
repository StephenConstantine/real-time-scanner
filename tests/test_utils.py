"""Tests for utility functions."""

import pytest
import os
import json
import tempfile
from unittest.mock import patch, mock_open
from modules.utils import (
    load_prompt, save_result, load_result, get_user_confirmation,
    sanitize_filename, format_timestamp
)


class TestLoadPrompt:
    """Test load_prompt function."""
    
    def test_load_existing_prompt(self, mock_prompts_file, monkeypatch):
        """Test loading an existing prompt."""
        # Mock the prompts file path
        mock_path = os.path.dirname(mock_prompts_file)
        monkeypatch.setattr('modules.utils.os.path.dirname', lambda x: mock_path)
        monkeypatch.setattr('modules.utils.os.path.join', 
                          lambda *args: mock_prompts_file if 'prompts.txt' in str(args) else os.path.join(*args))
        
        prompt = load_prompt("test_prompt")
        assert "This is a test prompt" in prompt
        assert "multiple lines" in prompt
    
    def test_load_nonexistent_prompt(self, mock_prompts_file, monkeypatch):
        """Test loading a non-existent prompt."""
        mock_path = os.path.dirname(mock_prompts_file)
        monkeypatch.setattr('modules.utils.os.path.dirname', lambda x: mock_path)
        monkeypatch.setattr('modules.utils.os.path.join', 
                          lambda *args: mock_prompts_file if 'prompts.txt' in str(args) else os.path.join(*args))
        
        with pytest.raises(ValueError, match="Prompt section 'nonexistent' not found"):
            load_prompt("nonexistent")
    
    def test_load_prompt_file_not_found(self, monkeypatch):
        """Test loading prompt when file doesn't exist."""
        monkeypatch.setattr('modules.utils.os.path.exists', lambda x: False)
        
        with pytest.raises(FileNotFoundError, match="Prompts file not found"):
            load_prompt("test_prompt")


class TestSaveResult:
    """Test save_result function."""
    
    def test_save_result_basic(self, temp_dir, monkeypatch):
        """Test basic result saving."""
        # Mock the results directory to use temp_dir
        monkeypatch.setattr('modules.utils.os.path.dirname', lambda x: temp_dir)
        
        test_data = {"test": "data", "value": 123}
        filepath = save_result(test_data, "test_step", "test_event")
        
        # Verify file was created
        assert os.path.exists(filepath)
        
        # Verify content
        with open(filepath, 'r') as f:
            loaded_data = json.load(f)
        assert loaded_data == test_data
        
        # Verify filename format
        filename = os.path.basename(filepath)
        assert "test_step" in filename
        assert "test_event" in filename
        assert filename.endswith(".json")
    
    def test_save_result_sanitize_event_name(self, temp_dir, monkeypatch):
        """Test event name sanitization in save_result."""
        monkeypatch.setattr('modules.utils.os.path.dirname', lambda x: temp_dir)
        
        test_data = {"test": "data"}
        filepath = save_result(test_data, "test_step", "Event With Spaces & Special!")
        
        filename = os.path.basename(filepath)
        # Should be sanitized to remove special characters
        assert "Event_With_Spaces__Special" in filename or "Event_With_Spaces_Special" in filename


class TestLoadResult:
    """Test load_result function."""
    
    def test_load_existing_result(self, temp_dir):
        """Test loading an existing result file."""
        test_data = {"test": "data", "number": 42}
        test_file = os.path.join(temp_dir, "test_result.json")
        
        # Create test file
        with open(test_file, 'w') as f:
            json.dump(test_data, f)
        
        # Load and verify
        loaded_data = load_result(test_file)
        assert loaded_data == test_data
    
    def test_load_nonexistent_result(self):
        """Test loading a non-existent result file."""
        with pytest.raises(FileNotFoundError, match="Result file not found"):
            load_result("/nonexistent/path/file.json")
    
    def test_load_invalid_json(self, temp_dir):
        """Test loading a file with invalid JSON."""
        test_file = os.path.join(temp_dir, "invalid.json")
        
        # Create file with invalid JSON
        with open(test_file, 'w') as f:
            f.write("invalid json content {")
        
        with pytest.raises(json.JSONDecodeError):
            load_result(test_file)


class TestGetUserConfirmation:
    """Test get_user_confirmation function."""
    
    @patch('builtins.input')
    def test_confirmation_yes(self, mock_input):
        """Test user confirmation with 'yes' input."""
        mock_input.return_value = 'y'
        result = get_user_confirmation("Test message")
        assert result is True
        
        mock_input.return_value = 'yes'
        result = get_user_confirmation("Test message")
        assert result is True
    
    @patch('builtins.input')
    def test_confirmation_no(self, mock_input):
        """Test user confirmation with 'no' input."""
        mock_input.return_value = 'n'
        result = get_user_confirmation("Test message")
        assert result is False
        
        mock_input.return_value = 'no'
        result = get_user_confirmation("Test message")
        assert result is False
    
    @patch('builtins.input')
    def test_confirmation_default_true(self, mock_input):
        """Test user confirmation with default True."""
        mock_input.return_value = ''  # Empty input
        result = get_user_confirmation("Test message", default=True)
        assert result is True
    
    @patch('builtins.input')
    def test_confirmation_default_false(self, mock_input):
        """Test user confirmation with default False."""
        mock_input.return_value = ''  # Empty input
        result = get_user_confirmation("Test message", default=False)
        assert result is False


class TestSanitizeFilename:
    """Test sanitize_filename function."""
    
    def test_sanitize_basic(self):
        """Test basic filename sanitization."""
        result = sanitize_filename("normal_filename.txt")
        assert result == "normal_filename.txt"
    
    def test_sanitize_spaces(self):
        """Test sanitizing spaces in filename."""
        result = sanitize_filename("file with spaces.txt")
        assert result == "file_with_spaces.txt"
    
    def test_sanitize_special_characters(self):
        """Test sanitizing special characters."""
        result = sanitize_filename("file@#$%^&*()name.txt")
        # Should remove special characters
        assert "@" not in result
        assert "#" not in result
        assert "filename" in result
    
    def test_sanitize_empty_string(self):
        """Test sanitizing empty string."""
        result = sanitize_filename("")
        assert result == ""
    
    def test_sanitize_only_special_chars(self):
        """Test sanitizing string with only special characters."""
        result = sanitize_filename("@#$%^&*()")
        assert result == ""


class TestFormatTimestamp:
    """Test format_timestamp function."""
    
    def test_timestamp_format(self):
        """Test timestamp format."""
        timestamp = format_timestamp()
        
        # Should be in YYYYMMDD_HHMMSS format
        assert len(timestamp) == 15  # YYYYMMDD_HHMMSS
        assert timestamp[8] == '_'  # Underscore separator
        
        # Should be numeric except for underscore
        parts = timestamp.split('_')
        assert len(parts) == 2
        assert parts[0].isdigit()  # Date part
        assert parts[1].isdigit()  # Time part
    
    @patch('modules.utils.datetime')
    def test_timestamp_specific_time(self, mock_datetime):
        """Test timestamp with specific time."""
        # Mock datetime to return specific time
        mock_datetime.now.return_value.strftime.return_value = "20240101_120000"
        
        timestamp = format_timestamp()
        assert timestamp == "20240101_120000"

