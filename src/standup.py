#!/usr/bin/env python3

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from constants import EMAIL, PASSWORD, PHONE_NUMBER, CARRIER, MESSAGE, SMTP_SERVER, SMTP_PORT
import os
import smtplib

SMS_GATEWAYS = {
    'verizon': 'vtext.com',
    'att': 'txt.att.net',
    'tmobile': 'tmomail.net',
    'sprint': 'messaging.sprintpcs.com',
    'boost': 'myboostmobile.com',
    'cricket': 'sms.cricketwireless.net',
    'uscellular': 'email.uscc.net',
    'metropcs': 'mymetropcs.com',
    'tracfone': 'mmst5.tracfone.com',
    'straight_talk': 'vtext.com',
    'google_fi': 'msg.fi.google.com'
}

def send_sms(phone_number, carrier, message):
    """
    Send SMS using email-to-SMS gateway
    """
    if carrier.lower() not in SMS_GATEWAYS:
        print(f"Unsupported carrier '{carrier}'. Supported carriers: {', '.join(SMS_GATEWAYS.keys())}")
        return False
    
    sms_email = f"{phone_number}@{SMS_GATEWAYS[carrier.lower()]}"
    
    try:
        msg = MIMEText(message, 'plain')
        msg['From'] = EMAIL
        msg['To'] = sms_email

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, sms_email, msg.as_string())
        server.quit()
        
        return True
        
    except Exception as e:
        print(f"Error sending SMS: {str(e)}")
        return False
    
def main():
    if not all([EMAIL, PASSWORD, PHONE_NUMBER, CARRIER]):
        print("Error: Missing required environment variables:")
        if not EMAIL:
            print("  - EMAIL")
        if not PASSWORD:
            print("  - PASSWORD")
        if not PHONE_NUMBER:
            print("  - PHONE_NUMBER")
        if not CARRIER:
            print("  - CARRIER")
        print("\nPlease set these environment variables before running the script.")

        return
    
    send_sms(PHONE_NUMBER, CARRIER, MESSAGE)

if __name__ == "__main__":
    main()