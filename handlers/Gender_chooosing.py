from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from create_bot import Gender
from create_bot import dp
@dp.message_handler(state=Gender.choosing)
async def choose_gender(msg:types.Message,state:FSMContext):
    if msg.text=='Mужчина':
        await state.update_data(gender='Mужчина',r_coef=0.68)
        await msg.answer('Введите рост (в см):',reply_markup=types.ReplyKeyboardRemove())
        await Gender.height.set()
    elif msg.text=='Женщина':
        await state.update_data(gender='Женщина',r_coef = 0.55)
        await msg.answer('Введите рост (в см):',reply_markup=types.ReplyKeyboardRemove())
        await Gender.height.set()
    else:
        await msg.answer("Пожалуйста, выберите пол Мужчины или Женщины")

def register_handlers_GenderChoosing(dp: Dispatcher):
    dp.register_message_handler(choose_gender, state=Gender.choosing)