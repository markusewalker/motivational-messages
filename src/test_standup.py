#!/usr/bin/env python3

from unittest.mock import patch, MagicMock
from standup import SMS_GATEWAYS
import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from standup import send_sms

@pytest.mark.unit
@patch('standup.smtplib.SMTP')
@patch('standup.EMAIL', 'test@example.com')
@patch('standup.PASSWORD', 'test_password')
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