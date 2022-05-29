import sqlite3 as sq
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot, dp
from keyboards.markups import inBuyMenu

def sql_start():
    global base, cur
    base = sq.connect('artwork.db')
    cur = base.cursor()
    if base:
        print('Database connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT, category TEXT)')
    base.commit()

async def sql_add_comand(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?,?)',tuple(data.values()))
        base.commit()
#Функции обращения к БД для каждой категории и вывода списка
async def sql_read_est(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 1').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read_tech(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 2').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read_artists(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 3').fetchall(): #fetchall выгружает данные в список
        print(ret)
        try:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)
        except:
            await bot.send_message('Раздел находится на модерации')

async def sql_read_other(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 4').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read_aero(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 5').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read_glina(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 6').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read_mini(message):
    for ret in cur.execute('SELECT * FROM menu WHERE category == 7').fetchall(): #fetchall выгружает данные в список
        print(ret)
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена:{ret[-2]}₽',reply_markup=inBuyMenu)

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?',(data,))
