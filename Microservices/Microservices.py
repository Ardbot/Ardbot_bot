from aiogram import types, Dispatcher

from bot.General.setting_bot.create_bot import bot


async def cmd_1111(message: types.Message):
    """ Стартововая функция """
    await bot.send_message(message.from_user.id, "Первая команда:")

async def cmd_2222(message: types.Message):
    """ Описание функции """
    await bot.send_message(message.from_user.id, "Вторая команда")


def register_handlers_microservices(dp: Dispatcher):
    dp.register_message_handler(cmd_1111, commands='11111')
    dp.register_message_handler(cmd_2222, commands='22222')

