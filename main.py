from aiogram import executor
from config import dp, bot
from handlers import  echo, commands,quiz



commands.register_commands(dp)
quiz.register_quiz_1(dp)
echo.register_echo(dp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
