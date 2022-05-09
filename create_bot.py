from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage #подходит для хранения нечувствительной информации, хранит в оперативной памяти

storage = MemoryStorage()
bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot,storage=storage)
