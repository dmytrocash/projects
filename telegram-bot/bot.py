# aiogram на данный момент лучшая для создания телеграм-ботов на пайтоне
from aiogram.utils.markdown import hlink
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
from config1 import TOKEN

# инициализируем объекты бота и диспетчера
bot = Bot(token=TOKEN) # создаём объект бота, в параметре которого передаём токен
dp = Dispatcher(bot) # нужен для управления handler-ами

# cоздаем message_handler и объявляем функцию ответа
@dp.message_handler(commands="start")
async def process_start_command(message: types.Message): # функция async всегда возвращает промис (промис – это специальный объект, который хранит своё состояние, текущий результат (если есть) и колбэки.)
    start_buttons = ["Вновь на складе"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) #уменьшаем размер кнопки
    keyboard.add(*start_buttons)
   
    await message.answer("Привет! Нажми на кнопку и я сгенерирую ссылку на товары, которые снова в наличии.", reply_markup=keyboard)

@dp.message_handler(Text(equals="Вновь на складе"))
async def get_link(message: types.Message):
    link = f"{hlink('http://localhost:8080/products')}"
    await message.answer(link) # await заставляет интерпретатор ждать до тех пор, пока промис справа не выполнится.

if __name__ == '__main__':
    executor.start_polling(dp) # запускаем бот
