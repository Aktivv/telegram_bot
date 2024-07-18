from config import dp, Admin, bot
from aiogram.utils import executor
import logging
from handlers import commands, echo, quiz

async def on_startup(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot started')

async def on_shutdown(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot stopped')


commands.register_commands(dp)
quiz.register_quiz(dp)


# Эхо функция - вызывать самым последним
echo.register_echo(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
