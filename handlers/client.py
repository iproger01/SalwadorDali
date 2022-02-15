from aiogram import types, Dispatcher
from create_bot import bot, dp

# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет твоческий человек")
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\n @SalwadorDalib ot ")

# @dp.message_handler(commands=['contact'])
async def command_contact(message : types.Message):
    await bot.send_message(message.from_user.id, "Звоните 88004430000")

# @dp.message_handler(commands=['address'])
async def command_address(message : types.Message):
    await bot.send_message(message.from_user.id, "Ростов-на-Дону, Тургеневская 5")

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(command_contact,commands=['contact'])
    dp.register_message_handler(command_address, commands=['address'])

