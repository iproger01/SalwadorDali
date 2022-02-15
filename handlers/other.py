from aiogram import types, Dispatcher
from create_bot import dp


# @dp.message_handler()
async def echo_send(message : types.Message):
    if "купить" in message.text.lower():
        await message.answer("Так так по-подробнее, что вы хотите купить?")

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)


    # if message.text == 'Привет':
    #     await message.answer('И тебе привет!') #ответ на сообщение
    # # await message.reply(message.text) #ответ на сообщение как ответ