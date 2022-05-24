
from loader import dp
from filters import IsGroup, is_admin
from aiogram import types
from random import random






@dp.message_handler(IsGroup(), text='Salom')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')
    
@dp.message_handler(IsGroup(),  text='Assalomualykum')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')
    



@dp.message_handler(IsGroup(), text='salom')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')
   


@dp.message_handler(IsGroup(), text='assalom')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')
    

@dp.message_handler(IsGroup(), text='Assalom')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')
    

@dp.message_handler(IsGroup(),text='assalomualeykum')
async def do_salom(message: types.Message):
    await message.reply('Vaaleykum salom')    
    

@dp.message_handler(IsGroup())
async def do_salom(message: types.Message):
    await message.reply(f'{message.text} novvi dagani  ')
