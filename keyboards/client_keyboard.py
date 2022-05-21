from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

# b1 = KeyboardButton('/Контакты')
# b2 = KeyboardButton('/Расположение')
# b3 = KeyboardButton('/Меню')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Поделиться геопозицей', request_location=True)
#
# kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #, one_time_keyboard=True)
# kb_client.add(b1).add(b2).insert(b3).row(b4,b5)

b1 = KeyboardButton('/Картины')
b2 = KeyboardButton('/Заказ портрета')
b3 = KeyboardButton('/Сертификаты')
b4 = KeyboardButton('/Сувениры')
b5 = KeyboardButton('/Адрес')
b6 = KeyboardButton('/Контакты и Соцсети')
b7 = KeyboardButton('/Написать художнику в лс ТГ')

kb_client_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_main.row(b1,b2).row(b3,b4).row(b5,b6).add(b7)