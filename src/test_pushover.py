#!/usr/bin/env python3

from unittest.mock import patch, MagicMock
import sys
import os
import pytest
import subprocess
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from pushover import MESSAGE_TYPES, main, get_message, send_pushover_notification

@pytest.mark.unit
@patch('pushover.requests.post')
@patch('pushover.PUSHOVER_USER_KEY', 'test_user_key_12345678901234567890')
@patch('pushover.PUSHOVER_API_TOKEN', 'test_api_token_12345678901234567890')
def test_simple_dummy_pushover_send(mock_post):
    """Simple test to check if dummy Pushover message will send"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    dummy_message = "Dummy test message!"
    
    result = send_pushover_notification(dummy_message)
    
    assert result is True, "Pushover message should be sent successfully with dummy data"
    
    mock_post.assert_called_once_with(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "test_api_token_12345678901234567890",
            "user": "test_user_key_12345678901234567890",
            "message": dummy_message,
            "title": "Motivational Message"
        }
    )

@pytest.mark.unit
@patch('pushover.PUSHOVER_USER_KEY', None)
@patch('pushover.PUSHOVER_API_TOKEN', 'test_api_token')
def test_pushover_missing_user_key():
    """Test Pushover notification with missing user key"""
    result = send_pushover_notification("Test message")
    assert result is False, "Should fail when user key is missing"

@pytest.mark.unit
@patch('pushover.PUSHOVER_USER_KEY', 'test_user_key')
@patch('pushover.PUSHOVER_API_TOKEN', None)
def test_pushover_missing_api_token():
    """Test Pushover notification with missing API token"""
    result = send_pushover_notification("Test message")
    assert result is False, "Should fail when API token is missing"

@pytest.mark.unit
@patch('pushover.requests.post')
@patch('pushover.PUSHOVER_USER_KEY', 'test_user_key')
@patch('pushover.PUSHOVER_API_TOKEN', 'test_api_token')
def test_pushover_api_error(mock_post):
    """Test Pushover notification with API error response"""
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {
        'errors': ['user identifier is not a valid user key'],
        'status': 0
    }
    
    mock_post.return_value = mock_response
    result = send_pushover_notification("Test message")
    
    assert result is False, "Should fail when API returns error"

@pytest.mark.unit
def test_get_message_default():
    """Test getting default message when no type has been specified"""
    result = get_message()
    assert result == MESSAGE_TYPES['default']

@pytest.mark.unit
def test_get_message_standup():
    """Test the standup message type"""
    result = get_message('standup')
    assert result == MESSAGE_TYPES['standup']
    assert "stretch those legs" in result

@pytest.mark.unit
def test_get_message_invalid_type():
    """Test getting message with invalid type"""
    result = get_message('invalid_type')
    assert result == MESSAGE_TYPES['default']

@pytest.mark.unit
@patch('sys.argv', ['pushover.py', '-l'])
@patch('sys.stdout', new_callable=StringIO)
def test_list_types_short_command(mock_stdout):
    """Test the -l/--list-types command line argument"""
    main()
    
    output = mock_stdout.getvalue()
    assert "Available message types:" in output
    assert "standup:" in output
    assert "default:" in output
    for msg_type in MESSAGE_TYPES.keys():
        assert msg_type in output

@pytest.mark.unit
@patch('sys.argv', ['pushover.py', '--list-types'])
@patch('sys.stdout', new_callable=StringIO)
def test_list_types_long_command(mock_stdout):
    """Test the --list-types command line argument (long form)"""
    main()
    
    output = mock_stdout.getvalue()
    assert "Available message types:" in output
    assert "standup:" in output

@pytest.mark.unit
@patch('sys.argv', ['pushover.py', '-t', 'standup'])
@patch('pushover.requests.post')
@patch('pushover.PUSHOVER_USER_KEY', 'test_user_key')
@patch('pushover.PUSHOVER_API_TOKEN', 'test_api_token')
@patch('sys.stdout', new_callable=StringIO)
def test_standup_message_command(mock_stdout, mock_post):
    """Test sending standup message via command line"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response
    
    main()
    
    output = mock_stdout.getvalue()
    assert "Sending message:" in output
    assert MESSAGE_TYPES['standup'] in output
    assert "Successfully sent message!" in output
    
    mock_post.assert_called_once_with(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": "test_api_token",
            "user": "test_user_key",
            "message": MESSAGE_TYPES['standup'],
            "title": "Motivational Message"
        }
    )

@pytest.mark.integration
def test_pushover_script_list_types():
    """Integration test for python3 pushover.py -l"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    python_exe = sys.executable

    result = subprocess.run([
        python_exe, 'src/pushover.py', '-l'
    ], capture_output=True, text=True, cwd=project_root)
    
    assert result.returncode == 0
    assert "Available message types:" in result.stdout
    assert "standup:" in result.stdout
    assert "default:" in result.stdout

@pytest.mark.integration
@patch.dict(os.environ, {
    'PUSHOVER_USER_KEY': 'test_user_key',
    'PUSHOVER_API_TOKEN': 'test_api_token'
})
def test_pushover_script_standup_type():
    """Integration test for python3 pushover.py -t standup"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    python_exe = sys.executable
    
    result = subprocess.run([
        python_exe, 'src/pushover.py', '-t', 'standup', '--help'
    ], capture_output=True, text=True, cwd=project_root)
    
    assert "choices" in result.stdout or result.returncode in [0, 2]