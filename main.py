import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import InputFile
from os import getenv
from dotenv import load_dotenv
from generate_valentine import generate_valentine

load_dotenv()

API_TOKEN = getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

state = {
    'page': 0,
    'from': None,
    'to': None
}


@dp.message_handler(lambda msg: state['page'] == 0)
async def start(message):
    state['page'] = 1
    print(message.chat)
    await message.answer(
        'Привет я Валентин, я могу сделать для тебя валентинку!\n \n Пожалуйста, введи имя отправителя: ')


@dp.message_handler(lambda msg: state['page'] == 1)
async def get_from(message):
    state['from'] = message.text
    state['page'] = 2
    await message.answer(
        'Пожалуйста, введи имя получателя: '
    )

@dp.message_handler(lambda msg: state['page'] == 2)
async def get_to(message):
    state['to'] = message.text
    image_title = generate_valentine(state['from'], state['to'])

    state['page'] = 0
    await bot.send_photo(chat_id=message.chat['id'], photo=InputFile(image_title))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
