from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import callback_query

from bot.Ardbot.markups.inline_ardbot import inl_kb_project, inl_kb_contacts
from bot.General.markups.inline_general import inline_kb1
from bot.General.setting_bot.create_bot import bot


async def cmd_project(message: types.Message):
    """ Список проектов"""
    await bot.send_message(message.from_user.id, "Список проектов:\n", reply_markup=inl_kb_project)

async def cmd_contacts(message: types.Message):
    """ Список проектов"""
    await bot.send_message(message.from_user.id, "Список контактов:\n", reply_markup=inl_kb_contacts)


async def call_test(callback_query: types.CallbackQuery):
    """ Обрабатываем колбек """
    await callback_query.message.answer('Нажата первая кнопка!', reply_markup=inline_kb1)
    await callback_query.answer('Сообщение в окошке!')


def register_handlers_ardbot_menu(dp: Dispatcher):
    dp.register_message_handler(cmd_project, commands='project')
    dp.register_message_handler(cmd_project, Text(equals="Проекты", ignore_case=True))
    dp.register_message_handler(cmd_contacts, commands='contacts')
    dp.register_message_handler(cmd_contacts, Text(equals="Контакты", ignore_case=True))

    """ Регистрация колбеков """
    dp.register_callback_query_handler(call_test, text="button1")
