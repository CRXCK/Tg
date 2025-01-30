import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

import os

TOKEN = 7839103259:AAFmxKA01JaiPIonoynWtwFjAZDwKnkttQo  # Используем переменную окружения
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот для доставки автотоваров в Мурманске.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
