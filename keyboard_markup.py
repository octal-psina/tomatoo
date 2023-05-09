#from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
#BTN_NEXT_PAGE = KeyboardButton('Next page', callback_data='next_page')


BTN_NEW_REQUEST = KeyboardButton('New request', callback_data='new_request')

BTN_TV_SHOWS = KeyboardButton('Tv series',callback_data='series')
BTN_THEATR = KeyboardButton('Movie in theatr', callback_data='theatr')
BTN_HOME = KeyboardButton('Movie at home', callback_data='home')

BTN_NEW = KeyboardButton('New',callback_data='new')
BTN_POPULAR = KeyboardButton('Popular', callback_data='popular')

BTN_GENRE_ACTION = KeyboardButton('Action', callback_data='action')
BTN_GENRE_ADVENTURE = KeyboardButton('Adventure', callback_data='adventur')
BTN_GENRE_ANIMATION = KeyboardButton('Animation', callback_data='animation')
BTN_GENRE_COMEDY = KeyboardButton('Comedy', callback_data='comedy')
BTN_GENRE_ROMANCE = KeyboardButton('Romance', callback_data='romance')
BTN_GENRE_CRIME = KeyboardButton('Crime', callback_data='crime')
BTN_GENRE_DOCUMENTARY = KeyboardButton('Documentary', callback_data='documentary')
BTN_GENRE_DRAMA = KeyboardButton('Drama', callback_data='drama')
BTN_GENRE_LGBTQ = KeyboardButton('Lgbtq', callback_data='lgbtq')
BTN_GENRE_HORROR = KeyboardButton('Horror', callback_data='horror')
BTN_GENRE_MUSIC = KeyboardButton('Music', callback_data='music')
BTN_GENRE_SCI_FI = KeyboardButton('Sci_fi', callback_data='sci_fi')
BTN_GENRE_WESTERN = KeyboardButton('Western', callback_data='western')

#NEXT_PAGE = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_NEXT_PAGE)
NEW_REQUEST = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_NEW_REQUEST)
OPTIONS = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_TV_SHOWS, BTN_THEATR, BTN_HOME)
FILTER = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_NEW, BTN_POPULAR)
#HELP = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_WEATHER, BTN_WIND).add(BTN_SUN_TIME)

GENRE_ROW = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_GENRE_ACTION,BTN_GENRE_ADVENTURE,BTN_GENRE_ANIMATION,BTN_GENRE_COMEDY,BTN_GENRE_ROMANCE,BTN_GENRE_CRIME,BTN_GENRE_DOCUMENTARY,BTN_GENRE_DRAMA,BTN_GENRE_LGBTQ,BTN_GENRE_HORROR,BTN_GENRE_MUSIC,BTN_GENRE_SCI_FI,BTN_GENRE_WESTERN)
#GENRE_ROW_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_GENRE_COMEDY,BTN_GENRE_ROMANCE,BTN_GENRE_CRIME)
#GENRE_ROW_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_GENRE_DOCUMENTARY,BTN_GENRE_DRAMA,BTN_GENRE_LGBTQ)
#GENRE_ROW_4 = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_GENRE_HORROR,BTN_GENRE_MUSIC,BTN_GENRE_SCI_FI)
#GENRE_ROW_5 = ReplyKeyboardMarkup(resize_keyboard=True).add(BTN_GENRE_WESTERN)

#GENRE_LGBTQ = ReplyKeyboardMarkup(resize_keyboard=True)
#GENRE_HORROR = ReplyKeyboardMarkup(resize_keyboard=True)
#GENRE_MUSIC = ReplyKeyboardMarkup(resize_keyboard=True)
#GENRE_SCI_FI = ReplyKeyboardMarkup(resize_keyboard=True)
#GENRE_WESTERN = ReplyKeyboardMarkup(resize_keyboard=True)


















