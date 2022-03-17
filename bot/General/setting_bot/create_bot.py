""" Прослойка для взаимодействия файлов """

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.General.setting_bot import config

""" Объявление и инициализация объектов бота и диспетчера """
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
