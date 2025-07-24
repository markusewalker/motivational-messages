import requests
from constants import PUSHOVER_USER_KEY, PUSHOVER_API_TOKEN
import os
import sys
import argparse

MESSAGE_TYPES = {
    'default': "Hope you are having a great day!",
    'standup': "Hourly reminder to get up and stretch those legs for at least 5 minutes!",
    'break': "Break time! Step away from work and enjoy your break!",
    'lunch': "Lunch time! Feed that belly!",
    'end_work_day': "Work day is over, time to log off!",
}

def get_message(message_type=None):
    """Returns the message based on the type specified, or the default message if no type is given"""
    key = message_type if message_type is not None else 'default'
    return MESSAGE_TYPES.get(key, MESSAGE_TYPES['default'])


def send_pushover_notification(message):
    """Sends the specified notification via Pushover API"""
    if not PUSHOVER_USER_KEY or not PUSHOVER_API_TOKEN:
        print("ERROR! Missing Pushover credentials...")
        return False

    try:
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": PUSHOVER_API_TOKEN,
            "user": PUSHOVER_USER_KEY,
            "message": message,
            "title": "Motivational Message",
        }
        
        response = requests.post(url, data=data)
        
        if response.status_code != 200:
            print(f"Pushover API Error (Status {response.status_code}):")
            try:
                error_details = response.json()
                print(f"  Response: {error_details}")
                if 'errors' in error_details:
                    for error in error_details['errors']:
                        print(f"  Error: {error}")
            except:
                print(f"  Raw response: {response.text}")
            return False
        
        return True
    except Exception as e:
        print(f"Error sending Pushover message: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Send a motivational message via Pushover')
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

    message = get_message(args.type)
    print(f"Sending message: {message}")
    success = send_pushover_notification(message)

    if success:
        print("Successfully sent message!")
    else:
        print("Failed to send message...")
        sys.exit(1)

if __name__ == "__main__":
    main()