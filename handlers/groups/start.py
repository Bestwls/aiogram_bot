
from loader import dp
from filters import IsGroup
from aiogram import types

@dp.message_handler(IsGroup(), commands=['start'])
async def do_start(message: types.Message):
    await message.reply('Siz guruhda start bosdingiz')



