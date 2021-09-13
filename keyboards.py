from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🗓Ro'yxatdan o'ting", callback_data="Bosildi")
        ]
    ]
)

contact_btn= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni yuborish☎️", request_contact=True),
        ],
        [
            KeyboardButton(text="◀️Orqaga")
        ],
    ], resize_keyboard=True
)

location_btn= ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Manzilingiz📍", request_location=True)
        ],
    ], resize_keyboard=True
)

photo_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Yuboring", callback_data="Yuborildi"),
            InlineKeyboardButton(text="❌Bekor qilish", callback_data="Bekor qilindi")
        ]
    ]
)
