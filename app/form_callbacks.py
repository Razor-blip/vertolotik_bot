from aiogram import types, Router, F

from forms import RegisterForm
from db_manager import add_user_to_db

forms_router = Router()

@RegisterForm.submit(router=forms_router)
async def register_form_submit_handler(form: RegisterForm):
    add_user_to_db(form.username, form.email, form.phone_number, form.account_type, form.password)

    await form.answer(
        text=f'Дякую, ви зареєстрували аккаунт під ніком: {form.username}! Тепер ви можете увійти до нього натиснувши сюди -> /start.',
        reply_markup=types.ReplyKeyboardRemove()
    )