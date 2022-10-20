from loader import dp
from aiogram.types import CallbackQuery
from data import db
from keyboards import inline, reply
from filters.states import MainStates
from aiogram.dispatcher import FSMContext
from utils import splitter
from datetime import datetime, timedelta


@dp.callback_query_handler(lambda call: "account_id" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
    title = "Error"
    for key, val in db.get_cryptos(call.message.chat.id).items():
        if str(val) == id:
            title = key
            break
    await call.message.answer(f"Название: {title}\nБаланс: {cash}", reply_markup=inline.account_btns(id))


@dp.callback_query_handler(lambda call: "edit" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    await MainStates.EDIT_STATE.set()
    async with state.proxy() as data:
        data["id"] = id
        await call.message.answer("Введите сумму")


@dp.callback_query_handler(lambda call: "go_back" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    title = "Error"
    
    for key, val in db.get_cryptos(call.message.chat.id).items():
        if str(val) == id:
            title = key
            break

    amount, comment = db.del_last_transaction(id)
    if amount is None:
        await call.message.answer("История полностью очищена")
    else:
        if str(eval(str(amount))) == str(amount).replace("+", "").replace("-", ""):
            await call.message.answer(f"Запись {title} {(eval(amount))} отменена", reply_markup=reply.menu())
        else:
            await call.message.answer(f"Запись {title} {amount} ({(eval(amount))}) отменена", reply_markup=reply.menu())


@dp.callback_query_handler(lambda call: "see_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    await call.message.answer("Выберите период", reply_markup=inline.see_history_btns(id))


@dp.callback_query_handler(lambda call: "delete_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    db.transaction_del(id)
    await call.message.answer("Вы очистили историю данного счёта", reply_markup=reply.menu())


@dp.callback_query_handler(lambda call: "delete_account" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    for key, val in db.get_cryptos(call.message.chat.id).items():
        if str(val) == id:
            db.crypto_del(key)
            await call.message.answer(f"Вы удалили счёт {key}", reply_markup=reply.menu())



#
#
#see_month_history


@dp.callback_query_handler(lambda call: "see_all_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    text = ''
    for id, data_ in db.get_transaction(id).items():
        text += data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
        if data_['amount'].replace("+", "", 1).isdigit() or \
        data_['amount'].replace("-", "", 1).isdigit():
            pass
        else:
            text += f" ({round(eval(data_['amount']), 2)})"
        text += f" {data_['comment']} \n"
    cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
    text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_dayly_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    text = ''
    for id, data_ in db.get_transaction(id).items():
        if timedelta(hours=24) + data_["datetime"] > datetime.now():
            text += data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
            if data_['amount'].replace("+", "", 1).isdigit() or \
            data_['amount'].replace("-", "", 1).isdigit():
                pass
            else:
                text += f" ({round(eval(data_['amount']), 2)})"
            text += f" {data_['comment']} \n"
    cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
    text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_week_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    text = ''
    for id, data_ in db.get_transaction(id).items():
        if timedelta(hours=168) + data_["datetime"] > datetime.now():
            text += data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
            if data_['amount'].replace("+", "", 1).isdigit() or \
            data_['amount'].replace("-", "", 1).isdigit():
                pass
            else:
                text += f" ({round(eval(data_['amount']), 2)})"
            text += f" {data_['comment']} \n"
    cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
    text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_month_history" in call.data, state="*")
async def dislike(call: CallbackQuery, state: FSMContext):
    await state.finish()
    _, id = call.data.split("|")
    text = ''
    for id, data_ in db.get_transaction(id).items():
        if timedelta(hours=720) + data_["datetime"] > datetime.now():
            text += data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
            if data_['amount'].replace("+", "", 1).isdigit() or \
            data_['amount'].replace("-", "", 1).isdigit():
                pass
            else:
                text += f" ({round(eval(data_['amount']), 2)})"
            text += f" {data_['comment']} \n"
    cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
    text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑'
    await splitter(call.message, text)