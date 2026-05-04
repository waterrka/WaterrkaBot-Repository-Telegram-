import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

async def start_handler(message: Message):
    await message.answer(f"Привет! Я WaterrkaBot🚀")

async def run_bot():
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        print("Ошибка: BOT_TOKEN не найден в .env файле.")
        return

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    dp.message.register(start_handler, CommandStart())

    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run_bot())