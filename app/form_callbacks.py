from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from forms import RegisterForm, LoginForm, OrderForm
from db_manager import add_user_to_db, is_user_authenticated, create_order
from keyboards import get_customer_menu
from states import AccountState

forms_router = Router()

@RegisterForm.submit(router=forms_router)
async def register_form_submit_handler(form: RegisterForm):
    add_user_to_db(form.username, form.email, form.phone_number, form.account_type, form.password)

    await form.answer(
        text=f'Дякую, ви зареєстрували аккаунт під ніком: {form.username}! Тепер ви можете увійти до нього натиснувши сюди -> /start.',
        reply_markup=types.ReplyKeyboardRemove()
    )

@LoginForm.submit(router=forms_router)
async def login_form_submit_handler(form: LoginForm, state: FSMContext):
    auth_data = is_user_authenticated(form.username, form.password)
    if auth_data:
        await form.answer("Вітаю! Ви успішно авторизувались у свій аккаунт")
        if auth_data == "customer":
            await form.answer("Для нагівації в боті ви можете скористатись меню нижче!",
                              reply_markup=get_customer_menu())
            await state.clear()
            await state.set_state(AccountState.customer)
            await state.update_data(username=form.username)
        else:
            #TODO add performer logic here
            pass
    else:
        await form.answer("Ви ввели неправильний пароль. Спробуйте ще раз -> /start")

@OrderForm.submit(router=forms_router)
async def order_form_submit_handler(form: OrderForm, state: FSMContext):
    data = await state.get_data()
    create_order(data.get("username", ""), form.task_name, form.description, form.price, "active")

    await form.answer("Вітаю! Замовлення було створено успішно. Слідкуйте за статусом вашого замовлення натиснувши на 'Переглянути прийняті замовлення'",
                      reply_markup=get_customer_menu())
    await state.clear()
    await state.set_state(AccountState.customer)