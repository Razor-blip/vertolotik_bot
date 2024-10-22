import os

import asyncio
from aiogram import Bot, Router, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv

from form_callbacks import forms_router
from keyboards import get_greet_keyboard
from keyboards import GreetKeyboard
from forms import RegisterForm

load_dotenv()

router = Router()
bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()

@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer("Вас вітає бот вертольотік, бажаєте зареєструватись чи увійти в існуючий аккаунт?",
                         reply_markup=get_greet_keyboard())
    
@forms_router.message(F.text == GreetKeyboard.REGISTER)
async def handle_register_callback(_, state: FSMContext):
    await RegisterForm.start(bot, state)

async def main():
    dp.include_router(router)
    dp.include_router(forms_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Start bot polling...")
    asyncio.run(main())