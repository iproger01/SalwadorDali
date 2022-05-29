from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inBuyMenu = InlineKeyboardMarkup(row_width=1)
btnBuyPicUrl = InlineKeyboardButton(text="Договориться о покупке", url= "https://t.me/Natali_art_Ust")
inBuyMenu.insert(btnBuyPicUrl)


inBookPortrait = InlineKeyboardMarkup(row_width=1)
btnBuyPortretUrl = InlineKeyboardButton(text="Договориться о заказе портрета", url= "https://t.me/Natali_art_Ust")
# btnMainMenu = InlineKeyboardButton(text="Главное меню", callback_data="send_main_menu")
inBookPortrait.insert(btnBuyPortretUrl)


inChatPainter = InlineKeyboardMarkup(row_width=1)
btnChatUrl = InlineKeyboardButton(text="Перейти в личные сообщения", url= "https://t.me/Natali_art_Ust")
inChatPainter.insert(btnChatUrl)