import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from aiogram import executor
from handlers import start, Gender_chooosing, Gender_height, Gender_weight, choose_drink, value_alc, stomach, long_time, spend_time, data
from create_bot import dp
from sqlite import db_start


class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_server():
    server = HTTPServer(('0.0.0.0', 8000), DummyHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()


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


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
