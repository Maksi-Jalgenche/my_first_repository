from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN

BOT_TOKEN = TOKEN

# Создаем объект бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду /start
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет! \nМеня зовут эхо-бот! \nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду /help
@dp.message(Command(commands=["help"]))
async def process_start_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь'
        ' \nИ в ответ я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на любые текстовые сообщения, кроме команд /start и /help
@dp.message()
async def process_start_command(message: Message):
    await message.reply(text=message.text)


# У нас будет другое имя
if __name__ == '__main__':
    print("Starting !!!")
    dp.run_polling(bot)


