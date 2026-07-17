from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

TOKEN = "BU_YERGA_BOT_TOKENINGIZ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "OshpazJobs botiga xush kelibsiz! 👨‍🍳"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
