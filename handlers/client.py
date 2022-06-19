import json
import string
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards.client_keyboard import kb_client_main
from database import sqlite_db
import keyboards.client_keyboard as nav
import keyboards.markups as inline


# @dp.message_handler(commands=['start','help'])
async def commands_start(message : types.Message, ):
    try:
        await bot.send_message(message.from_user.id, "Привет, я покажу картины Натали Устименко. Помогу приобрести абонемент на занятия или сувенир и помогу его отправить Вам. А также свяжу с художником, чобы Вы лично могли обговорить все нюансы заказа портрета или покупки. Воспользуйтесь меню.", reply_markup=kb_client_main)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\n @SalwadorDalibot ")
#список картин и кнопка Купить (перенаправляет на сообщение автору)
#Меню и возврат меню
async def bot_menu_message(message:types.Message):
    if message.text == 'Картины':
        await bot.send_message(message.from_user.id, 'Выберете раздел в меню', reply_markup=nav.kb_client_pic)
    elif message.text == 'Заказ портрета':
        await bot.send_message(message.from_user.id, 'Нажмите кнопку ниже и напишите:\n1.Размер желаемой работы (в сантиметрах)\n2.Количество лиц на портрете\n3.К какой дате нужна готовая работа  ', reply_markup=inline.inBookPortrait)
    elif message.text == 'Сертификаты':
        await bot.send_message(message.from_user.id, 'Выберете раздел в меню', reply_markup=nav.kb_cert_all)
    elif message.text == 'Сувениры':
        await bot.send_message(message.from_user.id, 'Выберете раздел в меню', reply_markup=nav.kb_client_pic)
    elif message.text == 'Адрес':
        await bot.send_message(message.from_user.id, "Ростов-на-Дону, Тургеневская 5")
    elif message.text == 'Контакты и соцсети':
        await bot.send_message(message.from_user.id, "Звоните 89526068971")
    elif message.text == 'Написать художнику в лс ТГ':
        await bot.send_message(message.from_user.id, 'Нажмите кнопку ниже и самостоятельно свяжитесь с художником, Натали обязательно Вам ответит ', reply_markup=inline.inChatPainter)
#Меню Картины
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Выберете раздел в меню', reply_markup=nav.kb_client_main)
    elif message.text == 'Серия работ ЭСТЕТИКА':
        await client_menu_comand(message)
    elif message.text == 'Серия работ TECH':
        await client_menu_tech(message)
    elif message.text == 'Портреты артистов':
        await client_menu_artists(message)
    elif message.text == 'Отдельные работы':
        await client_menu_other(message)
    elif message.text == 'Аэрография и роспись стен':
        await client_menu_aero(message)
#Меню сертификаты
    elif message.text == 'Подарочный сертификат на арт-свидание':
        await bot.send_photo(message.from_user.id, '/home/user/PycharmProjects/SalwadorDali/service/abonement.jpg', )
    elif message.text == 'Абонемент на занятия':
        await client_menu_tech(message)
    elif message.text == 'Подарочный сертификат на услуги художника':
        await client_menu_artists(message)
    elif message.text == 'Сертификат на пробное занятие':
        await client_menu_other(message)

    # else:
    #     await message.reply('Неизвестная команда')



# @dp.message_handler(commands=['contact'])
async def command_contact(message : types.Message):
    await bot.send_message(message.from_user.id, "Звоните 89526068971")

# @dp.message_handler(commands=['address'])
async def command_address(message : types.Message):
    await bot.send_message(message.from_user.id, "Ростов-на-Дону, Тургеневская 5")

#Вызов списков картин и кнопка Купить (перенаправляет на сообщение автору)
async def client_menu_comand(message: types.Message):
    await sqlite_db.sql_read_est(message)
async def client_menu_tech(message: types.Message):
    await sqlite_db.sql_read_tech(message)
async def client_menu_artists(message: types.Message):
    await sqlite_db.sql_read_artists(message)
async def client_menu_other(message: types.Message):
    await sqlite_db.sql_read_other(message)
async def client_menu_aero(message: types.Message):
    await sqlite_db.sql_read_aero(message)
# async def client_menu_glina(message: types.Message):
#     await sqlite_db.sql_read_glina(message)
# async def client_menu_mini(message: types.Message):
#     await sqlite_db.sql_read_mini(message)


@dp.callback_query_handler(text="send_main_menu")
async def send_main_menu(message : types.Message):
    await bot.send_message(message.from_user.id, 'Выберете раздел в меню', reply_markup=nav.kb_client_main)

# @dp.callback_query_handler(text="btnBuyPic")
# async def client_book_pic(message: types.Message):
#     await bot.forward_message(chat_id="@Tevil_AD", from_chat_id=update.message.chat_id, message_id=update.message.message_id)




# async def order_paining(message: types.Message):
#     await
#
# async def buy_certificates(message: types.Message):
#     await
#
# async def buy_souvenir(message: types.Message):
#     await
#
# async def write_to_painter(message: types.Message):
#     await


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start','help'])
    dp.register_message_handler(command_contact,commands=['Контакты-Соцсети'])
    dp.register_message_handler(command_address, commands=['Адрес'])
    # dp.register_message_handler(client_menu_comand, commands=['Картины'])
    dp.register_message_handler(bot_menu_message)
    dp.register_message_handler(send_main_menu)




