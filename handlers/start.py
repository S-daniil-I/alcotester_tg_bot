from aiogram import Bot,Dispatcher,executor,types
from create_bot import dp,Gender
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from sqlite import db_start,create_profile,edit_profile


@dp.message_handler(commands=['start'])
async def  cmd_start(msg: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Mужчина'))
    keyboard.add(KeyboardButton('Женщина'))
    await msg.answer("Выберите ваш пол:",reply_markup=keyboard)
    await create_profile(user_id=msg.from_user.id)

    await Gender.choosing.set()

@dp.message_handler(commands=['description'])
async def description_command(msg:types.Message):
    await msg.answer('<b>Внимание:</b> <em>Данный калькулятор служит исключительно для ознакомительных целей, предоставляя результат, </em>'
                     '<em>основанный на общепринятых формулах, таких как формула Видмарка. Результаты калькулятора являются </em>'
                     '<em>приблизительными и не заменяют профессиональной медицинской или юридической экспертизы, а также не служат </em>'
                     '<em>заменой анализа на содержание алкоголя в крови или медицинского освидетельствования. Выведение алкоголя у каждого человека </em>'
                     '<em>индивидуально и зависит от множества факторов, таких как время суток, усталость, перенесенные заболевания и другие.</em>',parse_mode='HTML')

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(description_command,commands=['description'])