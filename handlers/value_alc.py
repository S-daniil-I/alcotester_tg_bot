from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from create_bot import dp,Gender
from handlers.alc_kb import drink_keyboard

@dp.message_handler(state=Gender.value_alc)
async def input_volume(msg:types.Message,state:FSMContext):
    try:
        alc_value=int(msg.text)
        if alc_value<0:
            raise ValueError("Число должно быть положительным")
        data=await state.get_data()
        drink=data.get('current_drink')
        drinks=data.get('drinks',[])
        drinks.append({
            'drink': data['current_drink'],
            'volume': alc_value,
            'percentage': data['alc_percentage']
        })
        await state.update_data(value_alc=alc_value)
        await state.update_data(drinks=drinks)
        keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Добавить еще напиток ✅'))
        keyboard.add(KeyboardButton('Завершить выбор напитков ❌'))
        await msg.answer("Хотите добавить еще один напиток или завершить выбор?", reply_markup=keyboard)
        await Gender.confirm_drinks.set()
    except ValueError:
        await msg.answer("Введите объем числом в мл (например, 500).")

@dp.message_handler(state=Gender.confirm_drinks)
async def confirm_drinks(msg: types.Message, state: FSMContext):
    if msg.text == "Добавить еще напиток ✅":
        await msg.answer("Выберите следующий напиток:", reply_markup=drink_keyboard)
        await Gender.choose_drink.set()
    elif msg.text == "Завершить выбор напитков ❌":
        data = await state.get_data()
        drinks = data.get('drinks', [])
        drinks_text = "\n".join([f"{d['drink']}: {d['volume']} мл" for d in drinks])
        await msg.answer(f"Вы выбрали:\n{drinks_text}", reply_markup=types.ReplyKeyboardRemove())
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('На голодную'))
        keyboard.add(KeyboardButton('Средняя сытость'))
        keyboard.add(KeyboardButton('Плотно поел(а)'))
        await msg.answer("Выберите наполненность желудка:", reply_markup=keyboard)
        await Gender.stomach.set()
    else:
        await msg.answer("Пожалуйста, выберите один из вариантов: 'Добавить еще напиток' или 'Завершить выбор'.")

        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('На голодную'))
        keyboard.add(KeyboardButton('Средняя сытость'))
        keyboard.add(KeyboardButton('Плотно поел(а)'))
        await msg.answer("Выберите наполненность желудка:", reply_markup=keyboard)
        await Gender.stomach.set()

def value_alc(dp: Dispatcher):
     dp.register_message_handler(input_volume,state=Gender.value_alc)


def confirm_alc(dp: Dispatcher):
    dp.register_message_handler(confirm_drinks, state=Gender.confirm_drinks)





