from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from states import Users
from database import (
    get_leads,
    get_from_leads,
    update_status_manager_leads,
)
from keyboards import lead_keyboard
from aiogram import Bot


async def application(callback: types.CallbackQuery):
    leads = get_leads()

    if not leads:
        await callback.message.answer('Заявок пока нет.')
        await callback.answer()
        return

    await callback.message.answer('ТЕКУЩИЕ ЗАЯВКИ')
    for lead_id, description in leads:
        await callback.message.answer(
            f'📋 Заявка №{lead_id}\n📝 {description}',
            reply_markup=lead_keyboard(lead_id)
        )
    await callback.answer()


async def take_app(
    callback: types.CallbackQuery,
    state: FSMContext,
    bot: Bot,
):
    lead_id = int(callback.data.split('_')[1])
    manager_id = callback.from_user.id

    update_status_manager_leads('in_progress', manager_id, lead_id)

    await callback.message.answer(
        f'Вы приняли заявку №{lead_id}.\n'
        f'Напишите сообщение — оно уйдёт клиенту.'
    )
    await state.set_state(Users.write)
    await state.update_data(lead_id=lead_id)
    await callback.answer()


async def write(message: types.Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    lead_id = data.get('lead_id')

    if not lead_id:
        await message.answer('Ошибка: заявка не найдена.')
        await state.clear()
        return

    client_id = get_from_leads(lead_id)

    if not client_id:
        await message.answer('Клиент не найден.')
        await state.clear()
        return

    await bot.send_message(
        client_id,
        f'💬 Сообщение от менеджера по заявке №{lead_id}:\n\n{message.text}'
    )
    await message.answer('✅ Сообщение отправлено клиенту.')
    await state.clear()