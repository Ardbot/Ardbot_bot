from aiogram import types, Dispatcher

from bot.Admin.create_bot import bot


async def cmd_start(message: types.Message):
    """ Стартововая функция """
    await bot.send_message(message.from_user.id, "Добро пожаловать!\nМои услуги:")

async def cmd_website(message: types.Message):
    """ Ссылка на сайт """
    await bot.send_message(message.from_user.id, "Ссылка на сайт\nhttps://ardbot.github.io/")

async def cmd_project(message: types.Message):
    """ Список проектов"""
    await bot.send_message(message.from_user.id, "Список проектов:\n1)Бизнес с нуля")



def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_website, commands='website')
    dp.register_message_handler(cmd_project, commands='project')
