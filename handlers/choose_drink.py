from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher import FSMContext
from create_bot import dp,Gender
Alcohol_content = {
    'Безалкогольное пиво (0.5%)': 0.5,
    'Кефир старше 3х дней (0.7%)': 0.7,
    'Хлебный квас (0.5%)': 0.5,
    'Кумыс (1.2%)': 1.2,
    'Пиво лёгкое (4%)': 4,
    'Пиво обычное/Сидр (5%)': 5,
    'Пиво портер/тёмное (6%)': 6,
    'Слабоалкогольные напитки (7%)': 7,
    'Пиво крепкое (8%)': 8,
    'Шампанское (10%)': 10,
    'Вино (12%)': 12,
    'Вермут (Martini и пр.) (15%)': 15,
    'Мягкие ликёры (Baileys и пр.) (17%)': 17,
    'Портвейн (20%)': 20,
    'Средние ликёры (Malibu и пр.) (20%)': 20,
    'Рижский бальзам и т.п. (30%)': 30,
    'Крепкие ликёры (Jagermeister и т.п.) (35%)': 35,
    'Текила/Бренди/Бехеровка и т.п. (38%)': 38,
    'Ром (40%)': 40,
    'Джин (40%)': 40,
    'Водка (40%)': 40,
    'Коньяк (40%)': 40,
    'Виски/Бурбон/Скотч (40%)': 40,
    'Самбука (40%)': 40,
    'Абсент лёгкий (60%)': 60,
    'Абсент средний (69%)': 69,
    'Настойка боярышника (70%)': 70,
    'Абсент крепкий (80%)': 80,
    'Чистый спирт (95%)': 95
}



@dp.message_handler(state=Gender.choose_drink)
async def ch_drink(msg:types.Message,state: FSMContext):
    try:
        drink=msg.text
        alc_percantage=Alcohol_content[drink]
        await state.update_data(current_drink=drink,alc_percentage=alc_percantage)
        await msg.answer('Выберите объем,который вы употребили(мл):',reply_markup=types.ReplyKeyboardRemove())
        await Gender.value_alc.set()
    except KeyError:
        await msg.answer("Выбирайте только доступные напитки:")
def choose_drink(dp:Dispatcher):
    dp.register_message_handler(ch_drink,state=Gender.choose_drink)