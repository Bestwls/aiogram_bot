from loader import dp, bot, db
from aiogram import types
from states.translate import converter
from aiogram.dispatcher import FSMContext
from .converte import to_latin, to_cyrillic
from keyboards.default.lang import menu

@dp.message_handler(state=converter.menu)
async def convert(message: types.Message, state: FSMContext):
    msg=message.text
    await state.update_data(
        {'msg': msg},
    )
    await message.answer(f'Matnni kiriting')
    await converter.next()

@dp.message_handler(state=converter.convert)
async def to_latin1(message: types.Message, state: FSMContext):
    text=message.text 
    data=await state.get_data()
    if text.isascii():
        text=to_cyrillic(text)
        await message.answer(text, reply_markup=menu)
    else:
        text=to_latin(text)
        await message.answer(text, reply_markup=menu)
