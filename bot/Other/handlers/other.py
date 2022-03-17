from aiogram import Dispatcher, types

""" Хендлер последней инстанции """


async def other(message: types.Message):
    await message.answer('Я не знаю что это!\nНапиши сюда: @teh_ardbot')


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(other)
