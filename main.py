import setuptools
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes, ReplyKeyboardRemove, location
from keyboards import main_button, contact_btn, location_btn, photo_btn
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot


@dp.message_handler(commands="start", state="*")
async def do_start(message: types.Message, state: FSMContext):
    await state.finish()
    first_name = message.from_user.first_name
    await message.answer(f"Assalomu Alekum {first_name}\nRoyxatdan o'tish uchun pastdagi tugmani  bosing.",
                         reply_markup=main_button)


@dp.callback_query_handler(text="Bosildi")
async def get_button(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.message.answer("<b>Iltimos F.I.SH ni to'liq kiriting!\n\n</b>Masalan:<b>Salimov Salim Salimovich</b>")
    await state.set_state("name")


@dp.message_handler(state="name")
async def save_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("<b>Yoshingizni kiriting.</b>\n\nMasalan:<b>78 yosh</b>")
    await state.set_state("age")


@dp.message_handler(state="age")
async def get_age(message: types.Message, state: FSMContext):
    age = message.text
    try:
        age = int(age)
        await message.answer("Telefon raqamingizni kiriting", reply_markup=contact_btn)
        await state.update_data(age=age)
        await state.set_state("number")
    except:
        await message.answer("<b>Iltimos raqam kirgizing!</b>")
        await state.set_state("age")


@dp.message_handler(text="◀️Orqaga", state="number")
async def bac_to_age(message: types.Message, state: FSMContext):
    await message.answer("<b>Yoshingizni kiriting.</b>\n\nMasalan:<b>22</b>")
    await state.set_state("age")


@dp.message_handler(state="number", content_types=ContentTypes.CONTACT)
async def get_number(message: types.Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(number=number)
    await message.answer("Manzilingizni kirgizing", reply_markup=location_btn)
    await state.set_state("location")


@dp.message_handler(state="location", content_types=ContentTypes.LOCATION)
async def get_location(message: types.Message, state: FSMContext):
    longitude = message.location.longitude
    latitude = message.location.latitude
    map_url = f"google.com/maps?q={latitude},{longitude}"
    await state.update_data(location=map_url)
    await message.answer("Shaxsiy rasmingizni jonating", reply_markup=ReplyKeyboardRemove())
    await state.set_state("photo")


@dp.message_handler(state="photo", content_types=ContentTypes.PHOTO)
async def get_location(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    name = data.get("name")
    age = data.get("age")
    number = data.get("number")
    map_url = data.get("location")

    await message.answer_photo(photo=photo,caption=f"F.I.SH {name}\nYoshingiz: {age}\nTelefon raqmingiz: +{number}\nManzilingiz: {map_url}\n")
    await bot.send_photo(photo=photo,chat_id="1016399078", caption=f"F.I.SH {name}\nYoshingiz: {age}\nTelefon raqmingiz: +{number}\nManzilingiz: {map_url}\n")
    await state.finish()


@dp.message_handler(commands="help")
async def do_help(message: types.Message):
    await message.answer("Adminga murojaat qiling iltimos!\n@asadjuraev")


