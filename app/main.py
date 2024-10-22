import os

import asyncio
from aiogram import Bot, Router, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types.message import ContentType
from dotenv import load_dotenv

from form_callbacks import forms_router
from keyboards import get_greet_keyboard, GreetKeyboard, CustomerMenu, get_pay_order_button
from forms import RegisterForm, LoginForm, OrderForm
from states import states_router, AccountState
from db_manager import list_accepted_orders, get_order_by_id

load_dotenv()

router = Router()
bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()

@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer("Вас вітає бот вертольотік, бажаєте зареєструватись чи увійти в існуючий аккаунт?",
                         reply_markup=get_greet_keyboard())
    
@router.message(AccountState.customer, F.text == CustomerMenu.CHECK_ACCEPTED_ORDERS)
async def handle_check_accepted_orders(message: types.Message, state: FSMContext):
    data = await state.get_data()
    orders = list_accepted_orders(data.get("username"))

    if len(orders) == 0:
        await message.answer("У вас немає прийнятих замовлень")
    else:
        for order in orders:
            await message.answer(f"""Замовлення №{order.id}
Назва: {order.task_name}
Опис: {order.description}
Ціна: {order.price}
""", reply_markup=get_pay_order_button(order.id))
    
@forms_router.message(F.text == GreetKeyboard.REGISTER)
async def handle_register_callback(_, state: FSMContext):
    await RegisterForm.start(bot, state)

@forms_router.message(F.text == GreetKeyboard.LOGIN)
async def handle_register_callback(_, state: FSMContext):
    await LoginForm.start(bot, state)

@forms_router.message(AccountState.customer, F.text == CustomerMenu.CREATE_ORDER)
async def handle_create_order(_, state: FSMContext):
    await OrderForm.start(bot, state)

@router.callback_query(F.data.startswith("pay:"))
async def handle_pay_order_callback(callback_query: types.CallbackQuery):
    order_id = callback_query.data.split(":")[1]  # Extract the order ID
    order = get_order_by_id(order_id)

    await callback_query.message.answer(f"Оплата замовлення №{order_id} розпочата.")

    await bot.send_invoice(callback_query.message.chat.id,
                           title=order.task_name,
                           description=order.description,
                           provider_token=os.environ["TEST_PAYMENT_TOKEN"],
                           currency="UAH",
                           is_flexible=False,
                           prices=[types.LabeledPrice(label=f"{order.task_name}", amount=order.price*100)],
                           payload="test-invoice-payload")
    
@router.pre_checkout_query(lambda query: True)(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)

@router.message(F.content_type == ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платіж за замовлення на суму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} проведено успішно!")

async def main():
    dp.include_router(router)
    dp.include_router(forms_router)
    dp.include_router(states_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Start bot polling...")
    asyncio.run(main())