from aiogram3_form import Form, FormField

from keyboards import get_account_type_keyboard, get_phone_number_keyboard
from register_validators import validate_username, validate_email_adress, validate_phone_number, validate_password

class RegisterForm(Form):
    username: str = FormField(enter_message_text="Введіть username",
                              filter=validate_username,
                              error_message_text="Такий користувач вже зареєстрований. Будь ласка увійдіть в нього натиснувши сюди -> /start",)
    email: str = FormField(enter_message_text="Введіть Email",
                           filter=validate_email_adress,
                           error_message_text="Введено некоректний email! Спробуйте ще раз")
    phone_number: str = FormField(enter_message_text="Введіть номер телефону",
                                  filter=validate_phone_number,
                                  reply_markup=get_phone_number_keyboard(),
                                  error_message_text="Введено некоректний номер телефону!")
    password: str = FormField(enter_message_text="Придумайте пароль",
                              filter=validate_password,
                              error_message_text="Введено некоректний пароль!(пароль повинен містити букви та цифри)")
    account_type: str = FormField(enter_message_text="Виберіть тип аккаунту",
                                  reply_markup=get_account_type_keyboard())

