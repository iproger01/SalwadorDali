from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inBuyMenu = InlineKeyboardMarkup(row_width=1)
btnBuyPic = InlineKeyboardButton(text="Договориться о покупке", callback_data="btnBuyPic")

btnBuyPicUrl = InlineKeyboardButton(text="Договориться о покупке", url= "https://t.me/Natali_art_Ust")


inBuyMenu.insert(btnBuyPic)
inBuyMenu.insert(btnBuyPicUrl)

inBookPortrait = InlineKeyboardMarkup(row_width=1)
btnBuyPortretUrl = InlineKeyboardButton(text="Договориться о заказе портрета", url= "https://t.me/Natali_art_Ust")
btnMainMenu = InlineKeyboardButton(text="Главное меню", callback_data="send_main_menu")


inBookPortrait.insert(btnBuyPortretUrl)
inBookPortrait.insert(btnMainMenu)
