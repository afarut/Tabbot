from aiogram.dispatcher.filters.state import State, StatesGroup


class MainStates(StatesGroup):
	CRYPTO_CREATE_STATE = State()
	EDIT_STATE = State()