from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import BotCommand

from bot.General.markups import reply_general

""" Главная. Общие функции для сервисов """


async def set_commands(bot: Bot):
    """Установка команд для бота"""
    commands = [
        BotCommand(command="/cancel", description="Отмена"),
        BotCommand(command="/project", description="Мои проекты"),
        BotCommand(command="/help", description="Помощь")
    ]
    await bot.set_my_commands(commands)


async def cmd_start(message: types.Message, state: FSMContext):
    """ Стартовое сообщение """
    await state.finish()
    await message.answer("Приветствую!", reply_markup=reply_general.general_menu)

    with open('start_log.txt', mode='a', encoding='utf-8') as f:
        f.write(f"{message.from_user.id}'\n'")


async def cmd_cancel(message: types.Message, state: FSMContext):
    """ Отмена состояния машины и возврат в главное меню """
    await state.finish()
    await message.answer("Действие отменено", reply_markup=reply_general.general_menu)


async def cmd_help(message: types.Message):
    """ Помощь """
    await message.answer("Помощь\nВыберете сервис:")



async def other(message: types.Message):
    """Выполняется в последнюю очередь"""
    await message.answer('Я не знаю что это!\nНапиши сюда: @teh_ardbot')


async def callback_other(message: types.Message):
    """Выполняется в последнюю очередь"""
    await message.answer('Нераспознанный колбек')


def register_handlers_general_commands(dp: Dispatcher):
    """ Хендлеры. Общии команды для функций """
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_help, commands="help", state="*")
    dp.register_message_handler(cmd_help, Text(equals="Помощь", ignore_case=True))
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="Отмена", ignore_case=True))


def register_handlers_general_other(dp: Dispatcher):
    """ Хендлеры отмены. Выполняется последним """
    dp.register_message_handler(other)

    """ Регистрация колбеков """
    dp.register_callback_query_handler(callback_other)
