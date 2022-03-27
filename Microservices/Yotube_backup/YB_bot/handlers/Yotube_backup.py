import json
import time

import requests
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import message

from Microservices.Yotube_backup.YB_bot.markups.inline_general import inline_kb
from Microservices.Yotube_backup.Yotube import list_subs_channel, tg_log
from blog_notifications import list_tg
from bot.General.markups.reply_general import menu_cancel
from bot.General.setting_bot.config import id_channels
from bot.General.setting_bot.create_bot import bot


class YB_states(StatesGroup):
    """ Вход  в настройки """
    id_channels = State()
    subs_open = State()


async def call_start_yotube_backup(callback_query: types.CallbackQuery):
    """ Стартововая функция """
    await callback_query.message.answer("1) Откройте ссылку и скопируйте ID (идентификатор) канала.\n"
                                        "2) В разделе 'Конфиденциальность' ОТКРОЙТЕ информацию о подписках\n"
                                        "https://www.youtube.com/account_advanced\n")
    await callback_query.answer('Включен режим ожидания ID. Отмена /cancel')

    await YB_states.id_channels.set()


async def id_chek(message: types.Message, state: FSMContext):
    """ Проверка ид  """
    if message.text[:2] != 'UC':
        await bot.send_message(message.from_user.id, "Введен неверный ID.\nID адрес начинается с 'UC' ")
    # Первичная проверка адреса
    elif message.text[:2] == 'UC':
        data = list_subs_channel(message.text)
        status_code = data.get('status_code', 'no_code')
        mes = data.get('message', 'no_message')
        vrem = time.time_ns()
        id_channels = data.get('Yt_id', vrem)

        print(vrem)
        # print(data)

        # Всё норм, ответ получен
        if status_code == 200:
            with open(f'{id_channels}.txt', mode='w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            await bot.send_message(message.from_user.id, 'Отправляю документ.')
            # print('До')
            # time.sleep(10)
            # print('После')
            await message.reply_document(open(f'{id_channels}.txt', 'rb'))

            with open(f'{id_channels}.txt', 'r', encoding='utf-8') as f:
                data = json.loads(f.read())
                channel = data.get('channel')
                list_mes = []
                for item in channel:
                    title = item.get('title', '000')
                    list_mes.append(title)
                print(list_mes)

            list_mes = "\n".join(list_mes)

            await bot.send_message(message.from_user.id, list_mes[:4096])

            tg_log(message.from_user.id, message.text, status_code)

            # await bot.send_message(message.from_user.id,
            #                        'Подпишись на группу.Там будет инструкция на подписку к резервным каналам блогеров @ardbot_teh')
            await state.finish()
        # Открой доступ
        elif status_code == 403:
            await bot.send_message(message.from_user.id,
                                   f'Откройте подписки\nhttps://www.youtube.com/account_privacy\n')
            await bot.send_message(message.from_user.id, 'Введите ID.')
            tg_log(message.from_user.id, message.text, status_code)
        # Неверный адрес
        elif status_code == 404:
            await bot.send_message(message.from_user.id,
                                   f"Канал не найден: https://www.youtube.com/channel/{message.text}")
            await bot.send_message(message.from_user.id, 'Введите ID.')
            tg_log(message.from_user.id, message.text, status_code)
        # Другие ошибки (API, подключение...)
        else:
            await bot.send_message(message.from_user.id, f'Ошибка {status_code}\n{mes}')
            tg_log(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id,
                               f"Проверьте ссылку: https://www.youtube.com/channel/{message.text}")
        await bot.send_message(message.from_user.id, 'Введите ID.')

async def tess(message: types.Message):

    with open(f'{id_channels}.txt', 'rb') as f:
        data = json.loads(f.read())
        channel = data.get('channel')
        list_mes = []
        for item in channel:
            title = item.get('title', '000')
            list_mes.append(title)
        print(list_mes)

    # list_tg(id_channels)
    list_mes = "\n".join(list_mes)

    await bot.send_message(message.from_user.id, list_mes)

async def call_1(callback_query: types.CallbackQuery):
    """ Обрабатываем колбек """
    await callback_query.message.answer('Нажата первая кнопка!', reply_markup=inline_kb)
    await callback_query.answer('Сообщение в окошке!')


def register_handlers_yotube_backup(dp: Dispatcher):
    dp.register_message_handler(id_chek, state=YB_states.id_channels)

    dp.register_message_handler(tess, commands='tess')

    """ Регистрация колбеков """
    dp.register_callback_query_handler(call_start_yotube_backup, text="YT_backup", )
