from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create_bot import dp,Gender
TIME_OPTIONS = {
    'равномерно за час': 1,
    'равномерно за 2 часа': 2,
    'равномерно за 3 часа': 3,
    'равномерно за 4 часа': 4,
    'равномерно за 5 часов': 5,
    'равномерно за 6 часов': 6,
    'равномерно за 7 часов': 7,
    'равномерно за 8 часов': 8,
    'равномерно за 9 часов': 9,
    'равномерно за 10 часов': 10,
    'равномерно за 11 часов': 11,
    'равномерно за 12 часов': 12,
    'выпил все сразу': 0
}

@dp.message_handler(state=Gender.long_time)
async def long_time(msg:types.Message,state=FSMContext):
        time_long=msg.text
        time_long=TIME_OPTIONS[time_long]
        await state.update_data(time_long=time_long)
        keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Закончил только что'))
        keyboard.row(KeyboardButton('прошел 1 час'), KeyboardButton('прошло 2 часа'))
        keyboard.row(KeyboardButton('прошло 3 часа'), KeyboardButton('прошло 4 часа'))
        keyboard.row(KeyboardButton('прошло 5 часов'), KeyboardButton('прошло 6 часов'))
        keyboard.row(KeyboardButton('прошло 7 часов'), KeyboardButton('прошло 8 часов'))
        keyboard.row(KeyboardButton('прошло 9  часов'), KeyboardButton('прошло 11 часов'))
        keyboard.row(KeyboardButton('прошло 12 часов'), KeyboardButton('прошло 13 часов'))
        keyboard.row(KeyboardButton('прошло 14 часов'), KeyboardButton('прошло 15 часов'))
        keyboard.row(KeyboardButton('прошло 16 часов'), KeyboardButton('прошло 17 часов'))
        keyboard.row(KeyboardButton('прошло 18 часов'), KeyboardButton('прошло 19 часов'))
        keyboard.row(KeyboardButton('прошло 20 часов'), KeyboardButton('прошел 21 час'))
        keyboard.row(KeyboardButton('прошло 22 часа'), KeyboardButton('прошло 23 часа'))
        keyboard.add('Прошли сутки ')
        await msg.answer("Выберите время, которое прошло с  последнего момента употребления:", reply_markup=keyboard)
        await Gender.spend_time.set()


def long_time(dp:Dispatcher):
    dp.register_message_handler(long_time,state=Gender.long_time)
