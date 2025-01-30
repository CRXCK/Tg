from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для доставки автотоваров в Мурманске.")

executor.start_polling(dp, skip_updates=True)
