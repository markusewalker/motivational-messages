#!/usr/bin/env python3

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from constants import EMAIL, APP_PASSWORD, PHONE_NUMBER, CARRIER, SMTP_SERVER, SMTP_PORT
import os
import sys
import argparse
import smtplib

GATEWAYS = {
    'verizon': "vzwpix.com",
    'att': "txt.att.net",
    'tmobile': "tmomail.net",
    'sprint': "messaging.sprintpcs.com",
    'boost': "myboostmobile.com",
    'cricket': "sms.cricketwireless.net",
    'uscellular': "email.uscc.net",
    'metropcs': "mymetropcs.com",
    'tracfone': "mmst5.tracfone.com",
    'google_fi': "msg.fi.google.com"
}

MESSAGE_TYPES = {
    'default': "Hope you are having a great day!",
    'standup': "Hourly reminder to get up and stretch those legs for at least 5 minutes!",
    'break': "Break time! Step away from work and enjoy your break!",
    'lunch': "Lunch time! Feed that belly!",
    'end_work_day': "Work day is over, time to log off!",
}

def get_message(message_type=None):
    """
    Get message based on predefined type
    """
    if message_type and message_type in MESSAGE_TYPES:
        return MESSAGE_TYPES[message_type]

    return MESSAGE_TYPES['default']

def send_sms(phone_number, carrier, message):
    """
    Send SMS using email-to-SMS gateway
    """
    if carrier.lower() not in GATEWAYS:
        print(f"Unsupported carrier '{carrier}'. Supported carriers: {', '.join(GATEWAYS.keys())}")
        return False
    
    clean_phone = ''.join(filter(str.isdigit, phone_number))
    if clean_phone.startswith('1') and len(clean_phone) == 11:
        clean_phone = clean_phone[1:]

    sms_email = f"{clean_phone}@{GATEWAYS[carrier.lower()]}"
    
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = EMAIL
        msg['To'] = sms_email
        msg['Subject'] = ""
        
        text_part = MIMEText(message, 'plain')
        msg.attach(text_part)

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, APP_PASSWORD)
        
        for attempt in range(2):
            try:
                server.sendmail(EMAIL, [sms_email], msg.as_string())
                break
            except Exception as retry_e:
                if attempt == 1:
                    raise retry_e
                
        server.quit()

        return True
        
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Send motivational SMS messages')
    parser.add_argument('--type', '-t', 
                       choices=list(MESSAGE_TYPES.keys()),
                       help='Type of message to send')
    parser.add_argument('--list-types', '-l', 
                       action='store_true',
                       help='List available message types')
    
    args = parser.parse_args()
    
    if args.list_types:
        print("Available message types:")
        for msg_type, msg_text in MESSAGE_TYPES.items():
            print(f"  {msg_type}: {msg_text}")
        return
    
    if not all([EMAIL, APP_PASSWORD, PHONE_NUMBER, CARRIER]):
        print("Error: Missing required environment variables:")
        if not EMAIL:
            print("  - EMAIL")
        if not APP_PASSWORD:
            print("  - APP_PASSWORD")
        if not PHONE_NUMBER:
            print("  - PHONE_NUMBER")
        if not CARRIER:
            print("  - CARRIER")
        print("\nPlease set these environment variables before running the script.")
        return
    
    message_to_send = get_message(args.type)
    
    print(f"Sending message: {message_to_send}")
    success = send_sms(PHONE_NUMBER, CARRIER, message_to_send)
    
    if success:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS...")
        sys.exit(1)

if __name__ == "__main__":
    main()