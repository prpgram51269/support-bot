from config import BOT_TOKEN, PROXY
from handlers.manager import application, take_app, write
from handlers.client import write_lead, complaint
from states import Users
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher
import asyncio
from aiogram import F
from aiogram.filters import Command, StateFilter
from database import init_db
from handlers.admin import (
    all_check,
    new_application,
    in_process,
    ready,
    stat,
)
from handlers.start import cmd_start

session = AiohttpSession(proxy=PROXY)
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()

async def main():
    init_db()
    dp.callback_query.register(write_lead, F.data == 'question')
    dp.message.register(complaint, StateFilter(Users.complaint))

    dp.message.register(cmd_start, Command('start'))

    dp.callback_query.register(application, F.data == 'application')
    dp.callback_query.register(take_app, F.data.startswith('take_'))
    dp.message.register(write, StateFilter(Users.write))

    dp.callback_query.register(all_check, F.data == 'all_check')
    dp.callback_query.register(new_application, F.data == 'new')
    dp.callback_query.register(in_process, F.data == 'in_process')
    dp.callback_query.register(ready, F.data == 'ready')
    dp.callback_query.register(stat, F.data == 'stat')
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())