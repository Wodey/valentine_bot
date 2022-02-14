import logging
from aiogram import Bot, Dispatcher, executor
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = getenv('BOT_TOKEN')


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message):
    await message.answer('Hi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




