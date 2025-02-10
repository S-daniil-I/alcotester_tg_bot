from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from create_bot import dp, Gender,bot
from math import modf as m
from datetime import datetime
from sqlite import db_start,create_profile,edit_profile



def get_inform(value):
    range_dict={
    (0.01,0.19):"Вы практически трезвы!",
    (0.2,0.39): "Вы можете чувствовать себя слегка расслабленным, внутренние ограничения несколько ослабляются. После приема алкоголя настроение начинает подниматься.",
    (0.4,0.69): "Вы чувствуете тепло и расслабленность. Ваше поведение может быть более вызывающим: речь становится смелее и быстрее, а голос громче, чем обычно. Усиливаются эмоции – хорошее настроение становится еще лучше и точно так же усиливаются отрицательные эмоции. Вы можете ощущать легкую эйфорию. Мыслительные способности и память могут слегка нарушиться, делая вас неосмотрительным.",
    (0.7,0.99): "При этой степени опьянения начинаются нарушения равновесия, двигательных функций, четкости речи, скорости реакции, зрения и слуха. Нарушается самоконтроль и способность рассуждать, вы считаете, что действуете лучше обычного и вам трудно не продолжить пить. Вы можете чувствовать эйфорию.",
    (1.0,1.29): "У вас эйфория, хотя моторные функции, координация, скорость реакции и равновесие уже сильно нарушены. То же со способностью рассуждать и с памятью. В действительности вы не помните, сколько порций уже выпили. Ваши эмоции усиливаются. Некоторые люди становятся очень шумными и агрессивными.",
    (1.3,1.59): "Отсутствует равновесие, зрение затуманено, возникают трудности с передвижением и с речью. Мышление, восприятие и способность к принятию решений сильно нарушены. Эйфория понемногу проходит и сменяется неприятными чувствами, такими как тревожность, беспокойство, гнев и подавленность.",
    (1.6,1.99): "Вас наполняют сильные отрицательные эмоции, в результате вы можете стать агрессивным – и ненамеренно причинить вред себе или другим. На этой стадии могут образоваться т.н. провалы памяти – мозг больше не фиксирует происходящее. Моторные функции сильно нарушены.",
    (2.0,2.49): "Вам не скрыть спутанности сознания, бестолковости и неспособности понимать происходящее. Вам нужна помощь, чтобы встать или ходить. Если вы нанесете себе травму, то скорее всего не осознаете этого, поскольку не чувствуете боли. Вас тошнит или рвет (у некоторых эти симптомы могут возникнуть раньше). Поскольку рвотный рефлекс нарушен, есть опасность захлебнуться собственной рвотой. На этой стадии часты провалы памяти, поэтому вы, очевидно, на следующее утро ничего не вспомните.",
    (2.5,2.99): "Сильно нарушены все психические и физические функции, в том числе восприятие. Наступает эмоциональная бесчувственность. Повышен риск захлебнуться собственной рвотой, упасть и нанести себе серьезную травму или стать жертвой другого несчастного случая.",
    (3.0,3.49): "Вы в полубессознательном состоянии. Вы не понимаете, где находитесь. Вы можете внезапно потерять сознание, вас трудно привести в чувство.",
    (3.5,3.99): "Такая доза алкоголя действует как наркоз, используемый при операциях. Возможно, вы впадете в кому. Дыхание может стать прерывистым.",
    (4.0, float('inf')): "Нарушается работа сердца и дыхание. Фактически, вы в коме или уже мертвы."
}
    for key in range_dict:
        if key[0]<=value<=key[1]:
            return range_dict[key]
    return 'Не определено'

@dp.message_handler(state=Gender.data)
async def send_data(msg:types.Message,state=FSMContext):

    data= await state.get_data()

    drinks=data.get("drinks",[])
    gender=data.get("gender","не указан")
    height = data.get("height", "не указан")
    weight = data.get("weight", "не указан")
    # spend_time = data.get("spend_time", "не указано")
    time_long=data.get("time_long","не указано")
    choose_drink=data.get("drink","не указан")
    value_alc=data.get("value_alc","не указан")
    stomach_level=data.get("stomach","не указан")
    time_spend=data.get("time_spend","не указан")
    weight_foot=data.get('weight_foot','не указан')
    alc_percentage=data.get('alc_percentage','не указан')
    r_coef=data.get('r_coef',0)
    alc_cof_st=data.get('alc_cof_st','не указан')
    drinks_text = "\n".join([f"{d['drink']}: {d['volume']}мл " for d in drinks])
    A= sum([drink['volume'] * 0.033814 * (drink['percentage'] / 100) for drink in drinks])
    tm_sum=time_spend+time_long
    BAC_promille=(((A*5.14*alc_cof_st)/(weight_foot*r_coef))-(0.015*tm_sum))*10
    if BAC_promille<=0:
        BAC_promille=0.0
        await msg.answer(f'У вас {BAC_promille} промилле.Вы абсолютно трезвы!',reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
        return


    fractional_part,integer_part=m(BAC_promille/0.15)
    await state.update_data(
        BAC_promille=BAC_promille,
        integer_part=integer_part,
        fractional_part=fractional_part,
        current_time=datetime.now().strftime('%A, %d %B %Y г. в %H:%M')
    )
    await bot.send_message(
        msg.chat.id,
        text=(
            f"<b>Ваши данные:</b>\n"
            f"<b>Пол:</b> {gender}\n"
            f"<b>Рост:</b> {height} см\n"
            f"<b>Вес:</b> {weight} кг\n"
            f"<b>Вы употребляли:</b>\n{drinks_text}\n"
            f"<b>Наполнение желудка:</b> {stomach_level}\n"
            f"<b>Время с последнего употребления:</b> {time_spend} ч.\n"
            f"<b>Скорость употребления:</b> {time_long} ч.\n"
        ),
        reply_markup=types.ReplyKeyboardRemove(),
        parse_mode="HTML"
    )
    await  state.update_data(drinks=[])

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('Да,все верно ✅'))
    keyboard.add(KeyboardButton('Нет,заполнить заново ❌'))
    await msg.answer('Ваши данные корректные?', reply_markup=keyboard)
    await Gender.data_correct.set()

@dp.message_handler(state=Gender.data_correct)
async def correct_data(msg:types.Message,state=FSMContext):
    data = await state.get_data()
    BAC_promille = data.get('BAC_promille', 0.0)
    integer_part = data.get('integer_part', 0)
    fractional_part = data.get('fractional_part', 0.0)
    current_time = data.get('current_time', datetime.now().strftime('%A, %d %B %Y г. в %H:%M'))
    if msg.text == 'Да,все верно ✅':
        await bot.send_photo(chat_id=msg.chat.id,photo="https://i.yapx.ru/YZAT9.png",caption=
            f"По моим подсчетам, на текущий момент времени:\n"
            f"<b>Сейчас:</b> {datetime.now().strftime('%A, %d %B %Y г. в %H:%M')}\n\n"
            f"<b>Промилле:</b> {BAC_promille:.2f} %\n"
            f"Вы будете трезвы через <b>{int(integer_part)} ч {round(fractional_part * 60)} мин</b>\n"
            f"<b>На данном этапе опьянения характерно такое состояние:</b> {get_inform(BAC_promille)}",
            parse_mode="HTML",reply_markup=types.ReplyKeyboardRemove()
        )
        await edit_profile(state, user_id=msg.from_user.id)
        await state.finish()
    elif msg.text == 'Нет,заполнить заново ❌':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Mужчина'))
        keyboard.add(KeyboardButton('Женщина'))
        await msg.answer("Выберите ваш пол:", reply_markup=keyboard)
        await Gender.choosing.set()


def data(dp: Dispatcher):
    dp.register_message_handler(send_data,state=Gender.data)
    dp.register_message_handler(correct_data, state=Gender.data_correct)
