#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from bot.General.setting_bot.create_bot import dp, bot
from bot.Ardbot.handlers.menu_ardbot import register_handlers_ardbot_menu
from bot.General.handlers.cmd_general import set_commands, register_handlers_general_other, register_handlers_general_commands
from Microservices.Microservices import register_handlers_microservices
from Microservices.Yotube_backup.Yotube_backup import register_handlers_yotube_backup


async def on_startup():
    print(" Бот в онлайн ")


async def main():
    await on_startup()      # Уведомляем о старте
    await set_commands(bot)  # Устанавливаем команды бота (General)

    """ Регистрация основных хэндлеров """
    register_handlers_general_commands(dp)
    register_handlers_ardbot_menu(dp)

    """ Регистрация микросервисов """
    register_handlers_microservices(dp)
    register_handlers_yotube_backup(dp)


    """ Последний хендлер """
    register_handlers_general_other(dp)

    """ Запуск поллинга """
    await dp.start_polling()
    # await dp.skip_updates( )  # пропуск накопившихся апдейтов (необязательно)

    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
