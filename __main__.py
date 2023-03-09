import logging

from config import Config
from db import close_db

from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, filename="log.log")
logger = logging.getLogger(__name__)


def main():
    logger.info("starting...")
    logger.info("getting config...")
    config = Config()
    logger.info("config initialized...")
    logger.info("bot initializing...")
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    dp = Dispatcher(bot)
    dp.register_message_handler(callback = send_welcome, commands = ["start"])
     
    executor.start_polling(dp, skip_updates=True)

async def send_welcome(message: types.Message):
    await message.reply("Hi.\nHere you can reserve table in our restaurant, pusivlager")


try:
    main()
except:
    import traceback
    logger.warning(traceback.format_exc())
finally:
    close_db()
