from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
)

class GreetKeyboard:
    REGISTER = "Зареєструватись"
    LOGIN = "Увійти"

class AccountType:
    CUSTOMER = "Замовник"
    PERFORMER = "Виконавець"

class GetPhoneNumber:
    GETPHONENUMBER = "Поділитись контактом"

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