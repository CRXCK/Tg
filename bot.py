import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

import os

TOKEN = "7839103259:AAFmxKA01JaiPIonoynWtwFjAZDwKnkttQo"
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот для доставки автотоваров в Мурманске.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
products = {
    "Моторные масла": [
        {"id": 1, "name": "Масло Castrol 5W-30", "price": 2500, "description": "Синтетическое моторное масло.", "photo": "https://example.com/oil.jpg"},
        {"id": 2, "name": "Масло Mobil 1 0W-40", "price": 2800, "description": "Высококачественное масло для двигателей.", "photo": "https://example.com/mobil.jpg"}
    ],
    "Антифризы и охлаждающие жидкости": [
        {"id": 3, "name": "Антифриз G12 красный", "price": 1200, "description": "Охлаждающая жидкость для радиатора.", "photo": "https://example.com/antifreeze.jpg"}
    ]
}
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "7839103259:AAFmxKA01JaiPIonoynWtwFjAZDwKnkttQo"
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Кнопки выбора категории
@dp.message_handler(commands=['catalog'])
async def show_catalog(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    
    for category in products.keys():
        keyboard.add(InlineKeyboardButton(category, callback_data=f"category_{category}"))
    
    await message.answer("Выберите категорию товаров:", reply_markup=keyboard)

# Отображение товаров в категории
@dp.callback_query_handler(lambda call: call.data.startswith("category_"))
async def show_products(call: types.CallbackQuery):
    category = call.data.split("_")[1]
    items = products.get(category, [])
    
    if not items:
        await call.message.answer("В этой категории пока нет товаров.")
        return
    
    for item in items:
        text = f"<b>{item['name']}</b>\n💵 Цена: {item['price']} руб.\n📌 {item['description']}"
        await bot.send_photo(call.message.chat.id, item['photo'], caption=text)
    
    await call.answer()

executor.start_polling(dp, skip_updates=True)
@dp.callback_query_handler(lambda call: call.data.startswith("buy_"))
async def buy_product(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[1])
    
    for category, items in products.items():
        for item in items:
            if item["id"] == product_id:
                await call.message.answer(f"Вы выбрали: {item['name']}\n💰 Цена: {item['price']} руб.\nОплата через СБП.")
                return

    await call.answer("Ошибка: товар не найден.")
