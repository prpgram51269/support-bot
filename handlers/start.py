from aiogram import types
from config import ADMIN_IDS, MANAGER_IDS
from database import add_user, role_manager
from keyboards import client_kb, manager_kb, admin_kb

async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    if user_id in MANAGER_IDS:
        add_user(user_id, username)
        role_manager(user_id, role='manager')
        await message.answer(
            'Привет, менеджер. Выбери заявку клиента.',
            reply_markup=manager_kb
        )
    elif user_id in ADMIN_IDS:
        add_user(user_id, username)
        role_manager(user_id, role='admin')
        await message.answer(
            'Привет, админ.',
            reply_markup=admin_kb
        )
    else:
        add_user(user_id, username)
        await message.answer(
            'Привет! Спасибо, что пользуетесь нашим сервисом. '
            'Если вас мучает какая-то проблема или вопрос — спросите тут.',
            reply_markup=client_kb
        )