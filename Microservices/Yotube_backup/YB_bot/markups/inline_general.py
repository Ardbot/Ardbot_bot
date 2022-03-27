""" Кнопки под сообщением """
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn = InlineKeyboardButton('5555', callback_data='button1')
inline_kb = InlineKeyboardMarkup().add(inline_btn)

