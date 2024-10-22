from aiogram.fsm.state import State, StatesGroup
from aiogram import Router

states_router = Router()

class AccountState(StatesGroup):
    customer = State()
    performer = State()