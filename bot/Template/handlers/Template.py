from aiogram import types, Dispatcher
from bot.General.setting_bot.create_bot import bot
from bot.Template.markups.inline_general import inline_kb


async def cmd_1(message: types.Message):
    """ Стартововая функция """
    await bot.send_message(message.from_user.id, "Первая команда:")

async def cmd_2(message: types.Message):
    """ Описание функции """
    await bot.send_message(message.from_user.id, "текст")

async def call_1(callback_query: types.CallbackQuery):
    """ Обрабатываем колбек """
    await callback_query.message.answer('Нажата первая кнопка!', reply_markup=inline_kb)
    await callback_query.answer('Сообщение в окошке!')

def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(cmd_1, commands='1')
    dp.register_message_handler(cmd_2, commands='2')

    """ Регистрация колбеков """
    dp.register_callback_query_handler(call_1, text="button1")

