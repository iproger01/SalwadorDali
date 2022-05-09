import json
import string

from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards.client_keyboard import kb_client
from database import sqlite_db

# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "Привет твоческий человек", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\n @SalwadorDalibot ")

# @dp.message_handler(commands=['contact'])
async def command_contact(message : types.Message):
    await bot.send_message(message.from_user.id, "Звоните 88004430000")

# @dp.message_handler(commands=['address'])
async def command_address(message : types.Message):
    await bot.send_message(message.from_user.id, "Ростов-на-Дону, Тургеневская 5")

async def client_menu_comand(message: types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(command_contact,commands=['Контакты'])
    dp.register_message_handler(command_address, commands=['Расположение'])
    dp.register_message_handler(client_menu_comand, commands=['Меню'])


