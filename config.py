# Just change the info below and rename this file to config.py

from pyrogram import filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
TOKEN = os.environ['TOKEN']
SUDO_USERS = [int(admin) for admin in os.environ.get("ADMINS").split(" ")]
LOG_GROUP = None  # Just keep it like this if you are not going to use one

# No need to touch this
SUDO_FILTER = filters.user(SUDO_USERS)

LANG = "en"
