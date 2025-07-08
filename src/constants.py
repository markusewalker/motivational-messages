#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import os

EMAIL               = os.getenv('EMAIL')
PASSWORD            = os.getenv('PASSWORD')
PHONE_NUMBER        = os.getenv('PHONE_NUMBER')
CARRIER             = os.getenv('CARRIER')

SMTP_SERVER         = 'smtp.gmail.com'
SMTP_PORT           = 587

MESSAGE             = "Hourly reminder to get up and stretch those legs for at least 5 minutes!"