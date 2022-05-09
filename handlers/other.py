from aiogram import types, Dispatcher
from create_bot import dp
import json, os, string


# @dp.message_handler()
# async def echo_send(message : types.Message):
#     if "купить" in message.text.lower():
#         await message.answer("Так так по-подробнее, что вы хотите купить?")

# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('swearing.json')))) != set():
        await message.reply('Не стоит материться')
        await message.delete()

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

