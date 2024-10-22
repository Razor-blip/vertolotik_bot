import os

from aiogram import types
from aiogram.fsm.context import FSMContext
from email_validator import validate_email, EmailNotValidError
from phone_number_validator.validator import PhoneNumberValidator
from password_validator import PasswordValidator
from dotenv import load_dotenv

from db_manager import is_user_exists

load_dotenv()

validator = PhoneNumberValidator(api_key=os.environ["PHONE_NUMBER_VALIDATOR_API_KEY"])
schema = PasswordValidator()
schema.min(8).max(8).has().digits().letters()

async def validate_username(message: types.Message, state: FSMContext) -> str:
    if is_user_exists(message.text):
        await state.clear()
        return False

    return message.text

async def validate_email_adress(message: types.Message) -> str:
    try:
        emailinfo = validate_email(message.text, check_deliverability=True)
        email = emailinfo.normalized
        return email
    except EmailNotValidError as e:
        return False
    
async def validate_phone_number(message: types.Message) -> str:
    if message.contact is None:
        try:
            is_valid = validator.validate(message.text)
        except Exception as e:
            return False
    else:
        is_valid = validator.validate(message.contact.phone_number)

    if is_valid:
        return message.contact.phone_number
    else:
        return False
    
async def validate_password(message: types.Message) -> str:
    is_valid = schema.validate(message.text)

    if is_valid:
        return message.text
    else:
        return False