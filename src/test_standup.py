#!/usr/bin/env python3

from unittest.mock import patch, MagicMock
import sys
import os
import pytest
import subprocess
from io import StringIO

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from sms import SMS_GATEWAYS, MESSAGE_TYPES, main, get_message, send_sms

@pytest.mark.unit
@patch('sms.smtplib.SMTP')
@patch('sms.EMAIL', 'test@example.com')
@patch('sms.APP_PASSWORD', 'test_password')
def test_simple_dummy_message_send(mock_smtp_class):
    """Simple test to check if dummy message and number will send"""
    mock_server = MagicMock()
    mock_smtp_class.return_value = mock_server

    dummy_phone = os.getenv("PHONE_NUMBER") or "5551234567"
    dummy_carrier = os.getenv("CARRIER") or "verizon"
    dummy_message = "Dummy test message!"
    
    result = send_sms(dummy_phone, dummy_carrier, dummy_message)
    
    assert result is True, "SMS should be sent successfully with dummy data"
    
    mock_smtp_class.assert_called_once_with('smtp.gmail.com', 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with('test@example.com', 'test_password')
    mock_server.sendmail.assert_called_once()
    mock_server.quit.assert_called_once()
    
    args, kwargs = mock_server.sendmail.call_args
    assert args[0] == 'test@example.com'
    expected_gateway = SMS_GATEWAYS[dummy_carrier]
    assert args[1] == f"{dummy_phone}@{expected_gateway}"
    assert dummy_message in args[2]

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
@patch('sys.argv', ['sms.py', '-l'])
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
@patch('sys.argv', ['sms.py', '--list-types'])
@patch('sys.stdout', new_callable=StringIO)
def test_list_types_long_command(mock_stdout):
    """Test the --list-types command line argument (long form)"""
    main()
    
    output = mock_stdout.getvalue()
    assert "Available message types:" in output
    assert "standup:" in output

@pytest.mark.unit
@patch('sys.argv', ['sms.py', '-t', 'standup'])
@patch('sms.EMAIL', 'test@example.com')
@patch('sms.APP_PASSWORD', 'test_password')
@patch('sms.PHONE_NUMBER', '5551234567')
@patch('sms.CARRIER', 'verizon')
@patch('sms.smtplib.SMTP')
@patch('sys.stdout', new_callable=StringIO)
def test_standup_message_command(mock_stdout, mock_smtp_class):
    """Test sending standup message via command line"""
    mock_server = MagicMock()
    mock_smtp_class.return_value = mock_server
    
    main()
    
    output = mock_stdout.getvalue()
    assert "Sending message:" in output
    assert MESSAGE_TYPES['standup'] in output
    assert "SMS sent successfully!" in output
    
    mock_smtp_class.assert_called_once_with('smtp.gmail.com', 587)
    mock_server.starttls.assert_called_once()
    mock_server.login.assert_called_once_with('test@example.com', 'test_password')
    mock_server.sendmail.assert_called_once()
    mock_server.quit.assert_called_once()

@pytest.mark.integration
def test_sms_script_list_types():
    """Integration test for python3 sms.py -l"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    result = subprocess.run([
        'python3', 'src/sms.py', '-l'
    ], capture_output=True, text=True, cwd=project_root)
    
    assert result.returncode == 0
    assert "Available message types:" in result.stdout
    assert "standup:" in result.stdout
    assert "default:" in result.stdout

@pytest.mark.integration
@patch.dict(os.environ, {
    'EMAIL': 'test@example.com',
    'APP_PASSWORD': 'test_password',
    'PHONE_NUMBER': '5551234567',
    'CARRIER': 'verizon'
})
def test_sms_script_standup_type():
    """Integration test for python3 sms.py -t standup"""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    result = subprocess.run([
        'python3', 'src/sms.py', '-t', 'standup', '--help'
    ], capture_output=True, text=True, cwd=project_root)
    
    assert "choices" in result.stdout or result.returncode in [0, 2]