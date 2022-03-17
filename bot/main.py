#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from aiogram import Bot
from aiogram.types import BotCommand

from bot.Admin.create_bot import dp, bot
from bot.Client.handlers.menu import register_handlers_menu
from bot.Other.handlers.other import register_handlers_other


async def on_startup():
    print(" Бот в онлайн ")


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт"),
        BotCommand(command="/website", description="Сайт"),
        BotCommand(command="/project", description="Мои проекты")
    ]
    await bot.set_my_commands(commands)


async def main():
    await on_startup()      # Уведомляем о старте
    await set_commands(bot)  # Устанавливаем команды бота

    """ Регистрация основных хэндлеров """

    register_handlers_menu(dp)
    register_handlers_other(dp)

    """ Запуск поллинга """
    await dp.start_polling()
    # await dp.skip_updates( )  # пропуск накопившихся апдейтов (необязательно)

    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
