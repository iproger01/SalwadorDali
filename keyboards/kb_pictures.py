from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Серия работ ЭСТЕТИКА')
b2 = KeyboardButton('/Серия работ TECH')
b3 = KeyboardButton('/Портреты артистов')
b4 = KeyboardButton('/Отдельные работы')
b5 = KeyboardButton('/Аэрография и роспись стен')

kb_client_pic = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_pic.add(b1).add(b2).add(b3).add(b4).add(b5)