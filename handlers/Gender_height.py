from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from create_bot import dp,Gender
@dp.message_handler(state=Gender.height)
async def input_height(msg:types.Message,state:FSMContext):
    try:
        height_real=float(msg.text)
        if height_real <= 0:
            raise ValueError("Число должно быть положительным")
        await state.update_data(height=height_real)
        await msg.answer('Введите ваш вес(в кг):')
        await Gender.weight.set()
    except ValueError:
        await msg.answer('Пожалуйста,введите ваш рост положительным числом (например, 180)')

def gender_height(dp:Dispatcher):
    dp.register_message_handler(input_height,state=Gender.height)