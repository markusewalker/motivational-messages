from dotenv import load_dotenv
load_dotenv(dotenv_path=".env", override=True)

import os

PUSHOVER_USER_KEY   = os.getenv("PUSHOVER_USER_KEY")
PUSHOVER_API_TOKEN  = os.getenv("PUSHOVER_API_TOKEN")