from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from tomato_api import Napi_tomatto, walk
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
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    choose_category = State()
    choose_sort_type = State()
    choose_genre = State()

@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.answer(text="Hi!\nI'm EchoBot!\nPowered by aiogram.", reply_markup=kboard.NEW_REQUEST)


@dp.message_handler(text='New request')
async def echo(message: types.Message, state: FSMContext):
    await message.answer(text='Chose the type of show', reply_markup=kboard.OPTIONS)
    await state.set_state(Form.choose_category.state)

@dp.message_handler(state=Form.choose_category.state)
async def get_choose_category(message: types.Message, state: FSMContext):
    if message.text not in kboard.option_list:
        await message.answer(text ='Wrong input please use key board')
        return
    await state.update_data(choose_category=message.text)
    await message.answer('Data saved')
#    await state.reset_state(with_data=False)
    await message.answer(text='Chose new or popular', reply_markup=kboard.FILTER)
    await state.set_state(Form.choose_sort_type.state)

@dp.message_handler(state=Form.choose_sort_type.state)
async def get_choose_sort_type(message: types.Message, state: FSMContext):
    if message.text not in kboard.filter_list:
        await message.answer(text ='Wrong input please use key board')
        return
    await state.update_data(choose_sort_type=message.text)
    await message.answer('Data saved')
#    await state.reset_state(with_data=False)
    await message.answer(text='Chose genre wich you interest in', reply_markup=kboard.GENRE_ROW) 
    await state.set_state(Form.choose_genre.state)

@dp.message_handler(state=Form.choose_genre.state)
async def get_choose_genre(message: types.Message, state: FSMContext):
    if message.text.lower() not in kboard.genre_list:
        await message.answer(text ='Wrong input please use key board')
        return
    await state.update_data(choose_genre=message.text)
    await message.answer('Data saved')
    await state.reset_state(with_data=False)

@dp.message_handler(text="hey")
async def process_gender(message: types.Message, state: FSMContext):
    
    user_data = await state.get_data()
    await message.reply(f"Nice u done it {user_data}")
    # Finish conversation
   


if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
