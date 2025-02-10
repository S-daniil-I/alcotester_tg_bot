import sqlite3 as sq
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import dp, Gender, bot
from datetime import datetime
from math import modf as m

async def db_start():
    global db, cur

    db = sq.connect('bot_alcohol.db')
    cur = db.cursor()
    print("Подключение к базе данных установлено")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS profile (
            user_id TEXT PRIMARY KEY,
            gender TEXT,
            height TEXT,
            weight TEXT,
            alcohol TEXT,
            value TEXT,
            stomach TEXT,
            time_spend TEXT,
            time_long TEXT
        )
    """)
    db.commit()
    print("Таблица profile создана или уже существует")

async def create_profile(user_id):
    print(f"Проверка наличия профиля для user_id: {user_id}")
    user = cur.execute("SELECT 1 FROM profile WHERE user_id == ?", (user_id,)).fetchone()
    print(f"Результат проверки: {user}")
    if not user:
        cur.execute("INSERT INTO profile VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)", (user_id, '', '', '', '', '', '', '',''))
        db.commit()
        print(f"Профиль пользователя {user_id} создан")
    else:
        print(f"Профиль пользователя {user_id} уже существует")

async def edit_profile(state, user_id):
    async with state.proxy() as data:
        print(f"Обновление профиля для user_id: {user_id} с данными: {data}")
        cur.execute("""
            UPDATE profile
            SET gender = ?, height = ?, weight = ?, alcohol = ?,value=?, stomach = ?, time_spend = ?, time_long = ?
            WHERE user_id = ?
        """, (data['gender'], str(data['height']), int(data['weight']), str(data.get('current_drink', '0')),data.get("value_alc"," "), data['stomach'],
              str(data['time_spend']), str(data['time_long']), user_id))
        db.commit()

        print("Профиль пользователя обновлен")