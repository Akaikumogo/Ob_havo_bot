from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.default.keyboards import markup,back
from loader import dp

from states.search import search

import requests

@dp.message_handler(text="ℹ️ About")
async def answer(message: types.Message, state: FSMContext):
    await message.answer("Ushbu bot butun dunyodagi eng so'ngi ob havo ma'lumotlarini ko'rsatib beradi")
@dp.message_handler(text="🔍Izlash")
async def answer(message: types.Message, state: FSMContext):
    await search.search.set()
    await message.answer("""Marhamat qilib Davlat yoki shahar nomini kiriting
Misol uchun: "O'zbekiston" yoki "Toshkent"
Eslatib o'tamiz biz bilan butun
dunyo ob-havo ma'lumotlarini topishingiz mumkin""",reply_markup=back)

@dp.message_handler(state=search.search)
async def qidiruv(message: types.Message, state: FSMContext):
    if message.text== "Qidiruv bo'limidan chiqish":
        await state.finish()
        await message.answer('Siz asosiy menudasiz',reply_markup=markup)  

    else:
        try:
            if message.text== "Qidiruv bo'limidan chiqish":
                await state.finish()
                await message.answer('Siz asosiy menudasiz',reply_markup=markup)
            API = 'f441cb7b77702bb2d9648180922cae59'
            CITY = message.text
            URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&appid={API}'
            response = requests.get(url=URL).json()
            city_info = {
                'city': CITY,
               'temp': response['main']['temp'],
                'humidity': response['main']['humidity'],
                'weather': response['weather'][0]['main'],
                'wind': response['wind']['speed'],
                'pressure': response['main']['pressure'],
            }
            h={'Clear':'ochiq',
            "Clouds":"bulutli",
            "Snow":"qorli",
            "Mist":"tumanli",
            "Smoke":'tutunli',
            "Haze":"tumanli",
            "Dust":"havo changli",
            "Fog":"quyuq tuman mavjud",
            "Sand":"yuqori darajada changlangan",
            "Ash":"havo tarkibida kul miqdori ko'p",
            "Squall":"yomg'irli",
            "Tornado":"Bo'ron bo'lmoqda",
            "Rain":"yomg'irli",
            "Drizzle":"yomg'irli",
            "Thunderstorm":"chaqmoq va momaqaldiroq mavjud"
            }
            msg = f"""<b><u>{CITY.upper()}</u>

Ob-havo:{h[city_info['weather']]} </b>
------------------------------------
🌡 Harorat: <b>{city_info['temp']} C</b>
💨 Shamol: <b>{city_info['wind']} m/s</b>
💦 Namlik: <b>{city_info['humidity']} %</b>
🧬 Bosim: <b>{city_info['pressure']} hPa</b>"""
            await message.answer(msg, parse_mode='html',reply_markup=back)

        except Exception as e:
            msg1 = f"Ushbu davlat haqida ma'lumotlar mavjud emas"
            await message.answer(msg1, parse_mode='html',reply_markup=back)