from aiogram.fsm.state import State, StatesGroup


class Users(StatesGroup):
    complaint = State()
    write = State()