from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create_bot import dp,Gender
from handlers.data import send_data

TIME_OPTIONS = {
    'Закончил только что': 0,
    'прошел 1 час': 1,
    'прошло 2 часа': 2,
    'прошло 3 часа': 3,
    'прошло 4 часа': 4,
    'прошло 5 часов': 5,
    'прошло 6 часов': 6,
    'прошло 7 часов': 7,
    'прошло 8 часов': 8,
    'прошло 9 часов': 9,
    'прошло 11 часов': 11,
    'прошло 12 часов': 12,
    'прошло 13 часов': 13,
    'прошло 14 часов': 14,
    'прошло 15 часов': 15,
    'прошло 16 часов': 16,
    'прошло 17 часов': 17,
    'прошло 18 часов': 18,
    'прошло 19 часов': 19,
    'прошло 20 часов': 20,
    'прошел 21 час': 21,
    'прошло 22 часа': 22,
    'прошло 23 часа': 23,
    'Прошли сутки': 24
}
@dp.message_handler(state=Gender.spend_time)
async def spend_time(msg:types.Message,state=FSMContext):
    try:
        time_spend=msg.text
        time_spend = TIME_OPTIONS[time_spend]
        await state.update_data(time_spend=time_spend)
        await Gender.data.set()
        await send_data(msg, state)
    except KeyError:
        await msg.answer("Выбирайте только доступные варианты:")

def spend_time(dp:Dispatcher):
    dp.register_message_handler(spend_time,state=Gender.spend_time)