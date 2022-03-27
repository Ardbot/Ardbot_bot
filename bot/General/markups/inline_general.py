""" Кнопки под сообщением """
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

btn_project = [
    types.InlineKeyboardButton(text="Мой сайт", url="https://ardbot.github.io/"),
    # types.InlineKeyboardButton(text="Справочная Константиновки", url="https://t.me/konst_info"),
    InlineKeyboardButton('Микросервисы', callback_data='microservices')]
inl_kb_project = InlineKeyboardMarkup(row_width=1).add(*btn_project)    # Раскрываем список *


btn_contacts = [
    types.InlineKeyboardButton(text="Telegram", url="https://t.me/teh_Ardbot"),
    # types.InlineKeyboardButton(text="***@bk.ru", url="https://e.mail.ru/inbox/"),
    # types.InlineKeyboardButton(text="Донат", url="https://don.nat")
]
inl_kb_contacts = InlineKeyboardMarkup(row_width=1).add(*btn_contacts)    # Раскрываем список *