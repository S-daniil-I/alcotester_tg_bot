from aiogram import Bot,Dispatcher,executor,types
from config import tokena_api
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
bot = Bot(token=tokena_api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
class Gender(StatesGroup):
    choosing = State()
    male = State()
    female = State()
    weight = State()
    height = State()
    choose_drink = State()
    stomach = State()
    value_alc = State()
    long_time = State()
    spend_time = State()
    data = State()
    data_correct=State()
    confirm_drinks=State()
