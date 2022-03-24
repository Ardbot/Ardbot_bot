from aiogram import types, Dispatcher
from bot.General.setting_bot.create_bot import bot


async def cmd_1(message: types.Message):
    """ Стартововая функция """
    await bot.send_message(message.from_user.id, "Первая команда:")

async def cmd_2(message: types.Message):
    """ Описание функции """
    await bot.send_message(message.from_user.id, "текст")


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(cmd_1, commands='1')
    dp.register_message_handler(cmd_2, commands='2')

