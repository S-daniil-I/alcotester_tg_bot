from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create_bot import dp,Gender
from handlers.alc_kb import drink_keyboard
@dp.message_handler(state=Gender.weight)
async def inpyt_weigtht(msg:types.Message,state:FSMContext):
    try:
        weight_real=float(msg.text)
        if weight_real <= 0:
            raise ValueError("Число должно быть положительным")
        await state.update_data(weight=weight_real,weight_foot=weight_real*2.20462)
        await msg.answer("Выберите напиток который вы употребляли: ", reply_markup=drink_keyboard)
        await Gender.choose_drink.set()
    except ValueError:
        await msg.answer("Пожалуйста, введите ваш вес положительным числом (например, 75)")
def gender_weight(dp:Dispatcher):
    dp.register_message_handler(inpyt_weigtht,state=Gender.weight)