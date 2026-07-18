
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "OshpazJobs botiga xush kelibsiz!\n\n"
        "🌍 Tilni tanlang:\n"
        "🇺🇿 O'zbekcha\n"
        "🇷🇺 Русский"
    )
