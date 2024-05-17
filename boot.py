from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from keyboard import kb

from aiogram.dispatcher.filters import Text
from sql import bd_start, bd_add_account, bd_all_site

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


# Функция on_startup
async def on_startup(_):
    await bd_start()
    print('Bot working!')



# Главное меню
#@dp.message_handler(commands=['menu'])
#async def cmd_menu(msg: types.Message):
#    await msg.answer('', reply_markup=kb)

#Получение данных для нового аккаунта
@dp.message_handler(Text(equals="Добавить аккаунт"))
async def msg_add_account(msg: types.Message):
    await msg.reply("Место для ссылки:")
    await msg.delete()


#Вывод всех аккаунтов
@dp.message_handler(Text(equals="Список аккаунтов"))
async def msg_all_accounts(msg: types.Message):
    await msg.answer(str(bd_all_site()))
    await msg.delete()


#Старт
@dp.message_handler(commands=['start'])
async def msg_start(msg: types.Message):
    await msg.answer("Бот для отслежевания просмотров TikTok, для начала работы /menu", reply_markup=kb)
    await msg.delete()


#
@dp.message_handler(commands=['help'])
async def send_welcome(msg: types.Message):
    await msg.reply("тп - https://t.me/kitb0y ")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)