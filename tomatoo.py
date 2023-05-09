#from tomato_api import Napi_tomatto
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging
from aiogram import Bot, Dispatcher, executor, types
import config
import keyboard_markup as kboard
API_TOKEN = config.TOKEN
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(text = "Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup = kboard.NEW_REQUEST)

@dp.message_handler()
async def echo(message: types.Message):
  
  if message.text == 'New request':
    await message.answer(text='Chose the type of show', reply_markup=kboard.OPTIONS)
  elif message.text in kboard.option_list:
    await message.answer(text='Chose new or popular', reply_markup = kboard.FILTER)
  elif message.text in kboard.filter_list:
    await message.answer(text='Chose genre wich you interest in', reply_markup = kboard.GENRE_ROW)
  elif message.text.lower() in kboard.genre_list:
    await message.answer(text='Nice you done it',)
    # old style:
    # old style:
    # await bot.send_message(message.chat.id, message.text)
  #await message.answer(message.text)



if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
