#!/usr/bin/env python3

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import os

EMAIL               = os.getenv('EMAIL')
APP_PASSWORD        = os.getenv('APP_PASSWORD')
PHONE_NUMBER        = os.getenv('PHONE_NUMBER')
CARRIER             = os.getenv('CARRIER')

SMTP_SERVER         = "smtp.gmail.com"
SMTP_PORT           = 587