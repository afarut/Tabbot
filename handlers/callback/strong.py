from loader import dp
from aiogram.types import CallbackQuery
from data import db
from keyboards import inline, reply
from aiogram.dispatcher import FSMContext
from utils import splitter
from datetime import datetime, timedelta


@dp.callback_query_handler(lambda call: "all_history" == call.data)
async def dislike(call: CallbackQuery):
    await call.message.answer("Выберите период", reply_markup=inline.all_history_btns())


@dp.callback_query_handler(lambda call: "balance" == call.data)
async def dislike(call: CallbackQuery):
    text = ""
    for title, id in db.get_cryptos(call.message.chat.id).items():
        cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(id).values())))
        text += f'Текущий баланс счёта {title}: {cash}\n'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "delete" == call.data)
async def dislike(call: CallbackQuery):
    await call.message.answer("Подтвердите удаление всех счётов", reply_markup=inline.yes_btn())


@dp.callback_query_handler(lambda call: "see_all_history" == call.data)
async def dislike(call: CallbackQuery):
    text = ''
    for title, crypto_id in db.get_cryptos(call.message.chat.id).items():
        for id, data_ in db.get_transaction(crypto_id).items():
            text += f"{title}: " + data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
            if data_['amount'].replace("+", "", 1).isdigit() or \
            data_['amount'].replace("-", "", 1).isdigit():
                pass
            else:
                text += f" ({round(eval(data_['amount']), 2)})"
            text += f" {data_['comment']} \n"
        cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(crypto_id).values())))
        #text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑\n'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_dayly_history" == call.data)
async def dislike(call: CallbackQuery):
    text = ''
    for title, crypto_id in db.get_cryptos(call.message.chat.id).items():
        for id, data_ in db.get_transaction(crypto_id).items():
            if timedelta(hours=24) + data_["datetime"] > datetime.now():
                text += f"{title}: " + data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
                if data_['amount'].replace("+", "", 1).isdigit() or \
                data_['amount'].replace("-", "", 1).isdigit():
                    pass
                else:
                    text += f" ({round(eval(data_['amount']), 2)})"
                text += f" {data_['comment']} \n"
        cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(crypto_id).values())))
        #text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑\n'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_week_history" == call.data)
async def dislike(call: CallbackQuery):
    text = ''
    for title, crypto_id in db.get_cryptos(call.message.chat.id).items():
        for id, data_ in db.get_transaction(crypto_id).items():
            if timedelta(hours=168) + data_["datetime"] > datetime.now():
                text += f"{title}: " + data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
                if data_['amount'].replace("+", "", 1).isdigit() or \
                data_['amount'].replace("-", "", 1).isdigit():
                    pass
                else:
                    text += f" ({round(eval(data_['amount']), 2)})"
                text += f" {data_['comment']} \n"
        cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(crypto_id).values())))
        #text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑\n'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "see_month_history" == call.data)
async def dislike(call: CallbackQuery):
    text = ''
    for title, crypto_id in db.get_cryptos(call.message.chat.id).items():
        for id, data_ in db.get_transaction(crypto_id).items():
            if timedelta(hours=720) + data_["datetime"] > datetime.now():
                text += f"{title}: " + data_['datetime'].strftime("%Y.%m.%d") + f" {data_['amount']}"
                if data_['amount'].replace("+", "", 1).isdigit() or \
                data_['amount'].replace("-", "", 1).isdigit():
                    pass
                else:
                    text += f" ({round(eval(data_['amount']), 2)})"
                text += f" {data_['comment']} \n"
        cash = sum(list(map(lambda x: float(round(eval(x['amount']), 2)), db.get_transaction(crypto_id).values())))
        #text += f'————————————————\n Текущий баланс счёта ({cash}) 🤑\n'
    await splitter(call.message, text)


@dp.callback_query_handler(lambda call: "yes" == call.data)
async def dislike(call: CallbackQuery):
    for title, id in db.get_cryptos(call.message.chat.id).items():
        db.crypto_del(title)
    await call.message.answer("Все счета удалены!")


@dp.callback_query_handler(lambda call: "menu" == call.data)
async def dislike(call: CallbackQuery):
    await call.message.answer("Вы в главном меню", reply_markup=reply.menu())