from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup

from Microservices.Yotube_backup.YB_bot.handlers.Yotube_backup import register_handlers_yotube_backup
from bot.General.setting_bot.create_bot import bot




async def call_microservices(callback_query: types.CallbackQuery):
    """ Список микросервисов """
    await callback_query.message.answer('Список микросервисов', reply_markup=inl_kb_microservices)
    await callback_query.answer('')



btn_list_microservices = [
    types.InlineKeyboardButton(text="Копия подписок Yotube", callback_data='YT_backup'),
    # types.InlineKeyboardButton(text="***@bk.ru", url="https://e.mail.ru/inbox/"),
    # types.InlineKeyboardButton(text="Донат", url="https://don.nat")
]
inl_kb_microservices = InlineKeyboardMarkup(row_width=1).add(*btn_list_microservices)    # Раскрываем список *



def register_handlers_microservices(dp: Dispatcher):
    # dp.register_message_handler(cmd_1111, commands='test')
    # dp.register_message_handler(cmd_2222, commands='22222')

    """ Регистрация микросервисов """
    register_handlers_yotube_backup(dp)

    """ Регистрация колбеков """
    dp.register_callback_query_handler(call_microservices, text="microservices")
