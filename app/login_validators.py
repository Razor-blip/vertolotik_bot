from aiogram import types
from aiogram.fsm.context import FSMContext

from db_manager import is_user_exists

async def check_username(message: types.Message) -> str:
    if is_user_exists(message.text):
        return message.text

    return False