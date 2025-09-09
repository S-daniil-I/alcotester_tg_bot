import threading
import socket
from aiogram import executor
from handlers import start, Gender_chooosing, Gender_height, Gender_weight, choose_drink, value_alc, stomach, long_time, spend_time, data
from create_bot import dp
from sqlite import db_start


def dummy_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 8000))  # Render видит открытый порт
        s.listen()
        while True:
            conn, addr = s.accept()
            conn.close()

threading.Thread(target=dummy_server, daemon=True).start()


async def on_startup(_):
    await db_start()


start.register_handlers_start(dp)
Gender_chooosing.register_handlers_GenderChoosing(dp)
Gender_height.gender_height(dp)
Gender_weight.gender_weight(dp)
choose_drink.choose_drink(dp)
value_alc.value_alc(dp)
stomach.stomach(dp)
long_time.long_time(dp)
spend_time.spend_time(dp)
data.data(dp)

if __name__=="__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
