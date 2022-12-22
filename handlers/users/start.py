from aiogram import types
from keyboards.default.keyboards import markup
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!",
        parse_mode='html',
        reply_markup=markup)
