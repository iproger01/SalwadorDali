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

#Keybard Gift certificats
inline_kb_gift = InlineKeyboardMarkup(row_width=2)
inline_btn1 = InlineKeyboardButton('3000', callback_data='btn1')
inline_btn2 = InlineKeyboardButton('5000', callback_data='btn2')
inline_btn3 = InlineKeyboardButton('15000', callback_data='btn3')
inline_btn4 = InlineKeyboardButton('25000', callback_data='btn4')

#Keybard abonement_type
inline_kb_gift = InlineKeyboardMarkup(row_width=3)
inline_btn5 = InlineKeyboardButton('5', callback_data='btn5')
inline_btn6 = InlineKeyboardButton('8', callback_data='btn6')
inline_btn7 = InlineKeyboardButton('10', callback_data='btn7')
