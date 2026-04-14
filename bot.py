import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

def get_main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔗 Фишинг", callback_data="phishing")],
            [InlineKeyboardButton(text="💔 Кибербуллинг", callback_data="bullying")],
            [InlineKeyboardButton(text="👤 Груминг", callback_data="grooming")],
        ]
    )
    return keyboard

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🛡 *Цифровой щит*\n\nВыбери сценарий:", parse_mode="Markdown", reply_markup=get_main_menu())

@dp.callback_query(lambda c: c.data == "phishing")
async def phishing(callback: types.CallbackQuery):
    await callback.message.answer("❌ Не переходи по подозрительным ссылкам!")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "bullying")
async def bullying(callback: types.CallbackQuery):
    await callback.message.answer("✅ Заблокируй обидчика и сделай скриншот!")
    await callback.answer()

@dp.callback_query(lambda c: c.data == "grooming")
async def grooming(callback: types.CallbackQuery):
    await callback.message.answer("🚫 Прекрати общение с незнакомцем!")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
