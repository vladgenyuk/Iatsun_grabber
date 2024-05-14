import os
import dotenv
import json

from pathlib import Path

dotenv.load_dotenv()

ADMIN_TELEGRAM_ID = os.environ.get('ADMIN_TELEGRAM_ID')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_USERNAME = os.environ.get('BOT_USERNAME')

API_HASH = os.environ.get('API_HASH')
API_ID = os.environ.get('API_ID')

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

BOT_OVERWRITE_PASSWORD = os.environ.get('BOT_OVERWRITE_PASSWORD')

DELAY_GRABBER = 1000
LIMIT = 5

BASE_DIR = Path(__file__).resolve().parent.parent

DATE_FORMAT = '%d.%m.%Y'

BOT_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

USER_STATES = {}

with open(f'{BASE_DIR}/config.json', 'r') as file:
    CONFIG_JSON = json.load(file)

ADMIN_IDS = CONFIG_JSON.get('admin_ids')
LAST_IDS = CONFIG_JSON.get('last_ids')