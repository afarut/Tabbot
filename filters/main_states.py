from .states import MainStates
from aiogram.types import Message
from loader import dp
from data import db
from aiogram.dispatcher import FSMContext
from keyboards import reply


@dp.message_handler(state=MainStates.CRYPTO_CREATE_STATE)
async def text_msg(message: Message, state: FSMContext):
	db.crypto_create(message.chat.id, message.text)
	await message.answer(f"Счёт <b>{message.text}</b> создан", reply_markup=reply.menu())
	await state.finish()


@dp.message_handler(state=MainStates.EDIT_STATE)
async def text_msg(message: Message, state: FSMContext):
    command = message.text
    if " " in command:
    	lst = list(map(str, command.split(" ")))
    	command = lst[0]
    	comment = " ".join(lst[1:])
    else:
    	comment = ""
    data = await state.get_data()
    title = "Error"
    for key, val in db.get_cryptos(message.chat.id).items():
        if str(val) == data["id"]:
            title = key
            break
    try:
        eval(command)
        db.transaction_create(data["id"], command, comment)
        if "+" in str(eval(command)) or "-" in str(eval(command)) or "*" in command:
            await message.answer(f"{title} {command} ({round(eval(command), 2)}) запись внесена")
        else:
            await message.answer(f"{title} {command} запись внесена")
    except Exception as e:
        print(e)
        print(e.with_traceback())
        await message.answer("Введите верный аргумент для этой команды")
    await state.finish()