from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from loader import dp
from keyboards import reply


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    text = f"""Здравствуйте, {message.from_user.full_name}!
Я бот-счетовод 🧮
Мои скромные функции помогут вести учет личных финансов или расчетов с партнерами.
Для начала вам нужно создать новый счет 🤑, а затем внести в него нужные суммы.
Вы можете создать множество счетов, обозначив их как вам удобно
Приятного использования ✅"""
    await message.answer(text, reply_markup=reply.menu())