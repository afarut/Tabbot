from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def menu():
	keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.row(KeyboardButton('Новый счет 🤑'))
	keyboard.row(KeyboardButton('Текущие счета 🏦'))
	return keyboard