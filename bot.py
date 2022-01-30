# aiogram на данный момент лучшая для создания телеграм-ботов на пайтоне
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
import csv
from config import TOKEN
from parser import result

# инициализируем объекты бота и диспетчера
bot = Bot(token=TOKEN) # создаём объект бота, в параметре которого передаём токен
dp = Dispatcher(bot) # нужен для управления handler-ами

# cоздаем message_handler и объявляем функцию ответа
@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    start_buttons = ["Вновь на складе"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #уменьшаем размер кнопки
    keyboard.add(*start_buttons)

    await message.answer("Привет! Нажми на кнопку и я сгенерирую ссылку на товары с сайта snt.od.ua, которые снова в наличии.", reply_markup=keyboard)
    
result()

@dp.message_handler(Text(equals="Вновь на складе"))

async def get_link(message: types.Message):
    link = "http://localhost:8080/products"
    await message.answer(link)

if __name__ == '__main__':
    executor.start_polling(dp) # запускаем бот
