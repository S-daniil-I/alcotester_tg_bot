from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create_bot import dp,Gender
from handlers.long_time import TIME_OPTIONS

def create_time_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(text) for text in TIME_OPTIONS.keys()]
    for i in range(0, len(buttons), 2):
        row = buttons[i:i + 2]
        keyboard.row(*row)
    return keyboard
ALC_COF={
    'На голодную':0.9,
    'Средняя сытость':0.8,
    'Плотно поел(а)':0.7
}
@dp.message_handler(state=Gender.stomach)
async def stomach_level(msg:types.Message,state:FSMContext):
    try:
        stomach=msg.text
        alc_cof_st=ALC_COF[stomach]
        await state.update_data(stomach=stomach,alc_cof_st=alc_cof_st)
        keyboard = create_time_keyboard()
        await msg.answer("Выберите длительность употребления:", reply_markup=keyboard)
        await Gender.long_time.set()
    except KeyError:
        await msg.answer("Выбирайте только доступные варианты:")

def stomach(dp:Dispatcher):
    dp.register_message_handler(stomach_level,state=Gender.stomach)
