from aiogram.types import Message
from loader import dp
from keyboards import inline
from data import db
from filters.states import MainStates


@dp.message_handler()
async def text_msg(message: Message):
    s = message.text
    if s == "Текущие счета":
        data = db.get_cryptos(message.chat.id)
        await message.answer("Текущие счета:", reply_markup=inline.accounts_btns(data))
    elif s == "Новый счет":
        await message.answer("Введите название нового счёта")
        await MainStates.CRYPTO_CREATE_STATE.set()
    #await message.answer(s)