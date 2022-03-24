from aiogram import types, Dispatcher

from Microservices.Yotube_backup.Yotube import subscriptions
from bot.General.setting_bot.config import id_channels
from bot.General.setting_bot.create_bot import bot


async def cmd_start_yotube_backup(message: types.Message):
    """ Стартововая функция """
    await bot.send_message(message.from_user.id, "Старт резервного копирования ютуб каналов")
    data = subscriptions(id_channels)
    # await bot.send_message(message.from_user.id, open(f'{id_channels}.json', 'w'))
    await message.reply_document(open(f'{id_channels}.json', 'rb'))




async def cmd_2(message: types.Message):
    """ Описание функции """
    await bot.send_message(message.from_user.id, "текст")


def register_handlers_yotube_backup(dp: Dispatcher):
    dp.register_message_handler(cmd_start_yotube_backup, commands='start_YB')
    dp.register_message_handler(cmd_2, commands='2')
