from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def example_btns(url):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Example url', url=url)
    btn2 = InlineKeyboardButton('Example button', callback_data=f"example")
    keyboard.row(btn1)
    keyboard.row(btn2)
    return keyboard


def accounts_btns(data): 
    keyboard = InlineKeyboardMarkup()
    lst = []
    for key, val in data.items():
        lst.append(InlineKeyboardButton(key, callback_data=f"account_id|{val}"))
    keyboard.row(InlineKeyboardButton('История счетов', callback_data=f"all_history"))
    keyboard.row(InlineKeyboardButton('Баланс', callback_data=f"balance"))
    keyboard.row(InlineKeyboardButton('Удалить все счета', callback_data=f"delete"))
    keyboard.add(*lst)
    return keyboard


def account_btns(id):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Внести операцию', callback_data=f"edit|{id}")
    btn2 = InlineKeyboardButton('Отменить операцию', callback_data=f"go_back|{id}")
    btn3 = InlineKeyboardButton('История счета', callback_data=f"see_history|{id}")
    btn5 = InlineKeyboardButton('Удалить историю', callback_data=f"delete_history|{id}")
    btn4 = InlineKeyboardButton('Удалить счет', callback_data=f"delete_account|{id}")
    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
    keyboard.row(btn4)
    keyboard.row(btn5)
    return keyboard


def see_history_btns(id):
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Вся', callback_data=f"see_all_history|{id}")
    btn2 = InlineKeyboardButton('Сутки', callback_data=f"see_dayly_history|{id}")
    btn3 = InlineKeyboardButton('Неделя', callback_data=f"see_week_history|{id}")
    btn4 = InlineKeyboardButton('Месяц', callback_data=f"see_month_history|{id}")
    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
    keyboard.row(btn4)
    return keyboard


def all_history_btns():
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Вся', callback_data=f"see_all_history")
    btn2 = InlineKeyboardButton('Сутки', callback_data=f"see_dayly_history")
    btn3 = InlineKeyboardButton('Неделя', callback_data=f"see_week_history")
    btn4 = InlineKeyboardButton('Месяц', callback_data=f"see_month_history")
    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
    keyboard.row(btn4)
    return keyboard

def yes_btn():
    keyboard = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton('Удалить все счета!', callback_data=f"yes")
    btn2 = InlineKeyboardButton('В главное меню', callback_data=f"menu")
    keyboard.row(btn1)
    keyboard.row(btn2)
    return keyboard