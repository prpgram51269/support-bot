from aiogram import types

from database import (
    get_leads,
    get_leads_in_process,
    get_leads_ready,
    get_stats,
)
from keyboards import filters_kb


async def all_check(callback: types.CallbackQuery):
    await callback.message.answer(
        'Здравия желаю, админ. Выберите, какие заявки вам нужны.',
        reply_markup=filters_kb
    )
    await callback.answer()


async def new_application(callback: types.CallbackQuery):
    leads = get_leads()

    if not leads:
        await callback.message.answer('Заявок пока нет.')
        await callback.answer()
        return

    for lead_id, description in leads:
        await callback.message.answer(
            f'📋 Заявка №{lead_id}\n📝 {description}'
        )
    await callback.answer()


async def in_process(callback: types.CallbackQuery):
    leads = get_leads_in_process()

    if not leads:
        await callback.message.answer('Заявок пока нет.')
        await callback.answer()
        return

    for lead_id, description in leads:
        await callback.message.answer(
            f'📋 Заявка №{lead_id}\n📝 {description}'
        )
    await callback.answer()


async def ready(callback: types.CallbackQuery):
    leads = get_leads_ready()

    if not leads:
        await callback.message.answer('Заявок пока нет.')
        await callback.answer()
        return

    for lead_id, description in leads:
        await callback.message.answer(
            f'📋 Заявка №{lead_id}\n📝 {description}'
        )
    await callback.answer()


async def stat(callback: types.CallbackQuery):
    res = get_stats()

    await callback.message.answer(
        f"Новых заявок: {res['new']}\n"
        f"Заявок в работе: {res['in_progress']}\n"
        f"Закрытых заявок: {res['closed']}\n"
        f"Всего заявок: {res['total']}"
    )
    await callback.answer()