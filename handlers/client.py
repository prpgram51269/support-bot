from aiogram import types
from aiogram.fsm.context import FSMContext

from states import Users
from database import add_user_lead


async def write_lead(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('Напишите свою жалобу или вопрос.')
    await state.set_state(Users.complaint)
    await callback.answer()


async def complaint(message: types.Message, state: FSMContext):
    description = message.text
    user_id = message.from_user.id

    lead_id = add_user_lead(description, user_id)

    await message.answer(
        f'✅ Ваша заявка №{lead_id} успешно добавлена!\n'
        f'Ждите ответа от менеджера.'
    )
    await state.clear()