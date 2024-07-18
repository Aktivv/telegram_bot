from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_buttons = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=False,
                                    row_width=2).add(
    KeyboardButton('/start'), KeyboardButton('game'), KeyboardButton('/quiz'), KeyboardButton('/registration'))


cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton('Отмена'))
