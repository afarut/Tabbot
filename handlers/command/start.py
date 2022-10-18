from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from loader import dp
from keyboards import reply


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.full_name}!", reply_markup=reply.menu())