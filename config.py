from os import environ as env
from dotenv import load_dotenv


load_dotenv()


class Config:

    def __init__(self):
        self.TELEGRAM_BOT_TOKEN = env['TELEGRAM_BOT_TOKEN']
        self.TELEGRAM_ADMIN_ID = env.get('TELEGRAM_ADMIN_ID', '')
        self.TELEGRAM_CHANNEL_ID = env.get('TELEGRAM_CHANNEL_ID', '')
