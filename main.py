from lib2to3.pgen2.tokenize import group

from aiogram import executor
from config import dp, bot
from handlers import  echo, commands,quiz, store, FSM_store,webapp, group

from db import db_main

async def on_startup(_):
    await db_main.sql_create()

commands.register_commands(dp)
quiz.register_quiz_1(dp)
store.register_fsm_reg(dp)
FSM_store.register_store(dp)
webapp.register_handlers_webapp(dp)
group.register_group(dp)

echo.register_echo(dp)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
