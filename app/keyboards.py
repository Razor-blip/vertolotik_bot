from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
    InlineKeyboardMarkup, 
    InlineKeyboardButton
)

class GreetKeyboard:
    REGISTER = "Зареєструватись"
    LOGIN = "Увійти"

class AccountType:
    CUSTOMER = "Замовник"
    PERFORMER = "Виконавець"

class GetPhoneNumber:
    GETPHONENUMBER = "Поділитись контактом"

class CustomerMenu:
    CREATE_ORDER = "Створити замовлення"
    CHECK_ACCEPTED_ORDERS = "Переглянути прийняті замовлення"

class PerformerMenu:
    CHECK_ALL_ORDERS = "Переглянути замовлення"

class PayOrder:
    PAY_ORDER = "Оплатити замовлення"

def get_greet_keyboard():
    button_register = KeyboardButton(text=GreetKeyboard.REGISTER)
    button_login = KeyboardButton(text=GreetKeyboard.LOGIN)

    markup = ReplyKeyboardMarkup(
        keyboard=[[button_register, button_login]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return markup

def get_account_type_keyboard():
    button_customer = KeyboardButton(text=AccountType.CUSTOMER)
    button_performer = KeyboardButton(text=AccountType.PERFORMER)

    markup = ReplyKeyboardMarkup(
        keyboard=[[button_customer, button_performer]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return markup

def get_phone_number_keyboard():
    button_phone_number = KeyboardButton(text=GetPhoneNumber.GETPHONENUMBER, request_contact=True)

    markup = ReplyKeyboardMarkup(
        keyboard=[[button_phone_number]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return markup

def get_customer_menu():
    create_order_button = KeyboardButton(text=CustomerMenu.CREATE_ORDER)
    check_accepted_orders_button = KeyboardButton(text=CustomerMenu.CHECK_ACCEPTED_ORDERS)

    markup = ReplyKeyboardMarkup(
        keyboard=[[create_order_button, check_accepted_orders_button]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return markup

def get_pay_order_button(order_id):
    pay_order_button = InlineKeyboardButton(text="Оплатити замовлення", callback_data=f"pay:{order_id}")

    markup = InlineKeyboardMarkup(
        inline_keyboard=[[pay_order_button]]
    )
    return markup