from aiogram import types

#Клавиатура аккаунотов
kb = types.ReplyKeyboardMarkup(resize_keyboard=True).row(
    types.KeyboardButton(text='Добавить аккаунт', callback_data="add_account"),
    types.KeyboardButton(text='Список аккаунтов', callback_data="all_accounts"),
    )