from aiogram.dispatcher.filters import Text
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
    new_link = State()
    gap = State()


@dp.message_handler(commands=['start', 'help'])
async def start_message(message: types.Message):
    """First launch comand"""
    await message.answer(text="Hi!\nI can help you to choose tv show or movie.", reply_markup=kboard.NEW_REQUEST)


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel any action"""
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.\nTo restart enter: /start', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(text='New request')
async def start_new_request(message: types.Message, state: FSMContext):
    '''Start new request'''
    await message.answer(text='Chose the type of show', reply_markup=kboard.OPTIONS)
    await state.set_state(Form.choose_category.state)


@dp.message_handler(state=Form.choose_category.state)
async def get_choose_category(message: types.Message, state: FSMContext):
    '''Get user filter and await next'''
    if message.text not in kboard.option_list:
        await message.answer(text='Wrong input please use key board')
        return
    await state.update_data(choose_category=message.text)
    await message.answer('Data saved')
#    await state.reset_state(with_data=False)
    await message.answer(text='Chose new or popular', reply_markup=kboard.FILTER)
    await state.set_state(Form.choose_sort_type.state)


@dp.message_handler(state=Form.choose_sort_type.state)
async def get_choose_sort_type(message: types.Message, state: FSMContext):
    '''Get user filter and await next filter'''

    if message.text not in kboard.filter_list:
        await message.answer(text='Wrong input please use key board')
        return
    await state.update_data(choose_sort_type=message.text)
    await message.answer('Data saved')
#    await state.reset_state(with_data=False)
    await message.answer(text='Chose genre wich you interest in', reply_markup=kboard.GENRE_ROW)
    await state.set_state(Form.choose_genre.state)


@dp.message_handler(state=Form.choose_genre.state)
async def get_choose_genre(message:
                           types.Message, state: FSMContext):
    '''Save user_genre input and processing gathered data'''
    n = Napi_tomatto()

    if message.text.lower() not in kboard.genre_list:
        await message.answer(text='Wrong input please use key board')
        return
    await state.update_data(choose_genre=message.text)
    await message.answer('Data saved')

    # creating link for request to websiet rotten tomatoes
    # stop saving process
    await state.reset_state(with_data=False)
    # get data frome storage
    user_data = await state.get_data()
    # creating link for request to websiet rotten tomatoes
    created_url = n.link_creator(user_data['choose_category'].lower(), user_data['choose_sort_type'].lower(),
                                 user_data['choose_genre'].lower())
    # start saving process
    await state.set_state(Form.new_link.state)
    # save output frome method link_creator()
    await state.update_data(new_link=created_url)
    # stop saving process
    await state.reset_state(with_data=False)
    # get data from storage
    user_data = await state.get_data()
    await message.reply(f"Ok let's check if is everything fine\nShow type: {user_data['choose_category']}\nFilter type: {user_data['choose_sort_type']}\nGenre: {user_data['choose_genre']}", reply_markup=kboard.CONFIRM)
    await state.set_state(Form.new_link.state)


@dp.message_handler(lambda message: message.text not in ['Confirm', 'Next page'], state=Form.new_link)
async def process_age_invalid(message: types.Message):
    return await message.reply("I dont't know what to do!")


@dp.message_handler(text='Confirm', state=Form.new_link)
#@dp.message_handler(text="hey")
async def get_n_send_info(message: types.Message, state: FSMContext):
    '''Get json file from rotton tomatoes and send it to user'''
    n = Napi_tomatto()
    # await state.set_state(Form.new_link.state)
    # await state.update_data(new_link="pupa")
    # await state.reset_state(with_data=False)
    user_data = await state.get_data()
    movies = n.napi_appeal(user_data['new_link'])  # user_data['new_link']
    for movie in movies[:-1]:
        #    print(movie)
        await message.answer(text=''.join(movie))
    if movies[-1] == True:
        await message.answer('Do you want to proceed?', reply_markup=kboard.NEXT_PAGE)
    elif movies[-1] == False:
        return await message.answer('Sorry, pages are over', reply_markup=kboard.CANCEL)

    # await message.reply(f"Nice u done it \n{user_data['choose_category']}\n{user_data['choose_sort_type']},\n{user_data['choose_genre']}\n{user_data['new_link']}")


@dp.message_handler(text='Next page', state=Form.new_link)
async def get_next_page(message: types.Message, state: FSMContext):
    n = Napi_tomatto()
    user_data = await state.get_data()
    next_page_link = n.get_next_page(user_data['new_link'])

    await state.set_state(Form.new_link.state)
    # save output frome method link_creator()
    await state.update_data(new_link=next_page_link)
    await message.answer(f"Do you want to proceed?", reply_markup=kboard.CONFIRM)
    print(user_data['new_link'] + '\n' + next_page_link)
    await state.set_state(Form.new_link.state)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)

# Удалить с гита токен бота дибил!!!
