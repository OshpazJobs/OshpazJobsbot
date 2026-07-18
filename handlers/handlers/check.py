from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

router = Router()


@router.callback_query(lambda c: c.data == "check_sub")
async def check_subscription(callback: CallbackQuery):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👨‍🍳 Ish qidiraman",
                    callback_data="job_search"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏢 Oshpaz kerak",
                    callback_data="need_cook"
                )
            ]
        ]
    )

    await callback.message.edit_text(
        "✅ Obuna tasdiqlandi!\n\n"
        "Kerakli bo‘limni tanlang:",
        reply_markup=keyboard
    )

    await callback.answer()
