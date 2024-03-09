from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F
from config import TOKEN

BOT_TOKEN = TOKEN

# Создаем объект бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

"""# Этот хэндлер будет срабатывать на команду /start
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
"""


async def process_start_command(message: Message):
    await message.answer('Привет! \nМеня зовут эхо-бот! \nНапиши мне что-нибудь')


async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь'
        ' \nИ в ответ я пришлю тебе твое сообщение')


async def send_echo(message: Message):
    await message.reply(text=message.text)


# Этот хэндлер будет будет срабатывать на отправку боту фото
async def send_photo_echo(message:Message):
    print(message)
    await message.reply_photo(message.photo[0].file_id)


# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_echo)

# У нас будет другое имя
if __name__ == '__main__':
    print("Starting !!!")
    dp.run_polling(bot)
