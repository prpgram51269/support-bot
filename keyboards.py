from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ask_btn = InlineKeyboardButton(text='Оставить заявку', callback_data='question')
client_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [ask_btn]
    ]
)

application_btn = InlineKeyboardButton(text='Посмотреть заявки', callback_data='application')
manager_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [application_btn]
    ]
)

all_application_btn = InlineKeyboardButton(text='Все заявки', callback_data='all_check')
statistic_btn = InlineKeyboardButton(text='Статистика', callback_data='stat')
admin_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [all_application_btn, statistic_btn]
    ]
)

new_btn = InlineKeyboardButton(text='Новые', callback_data='new')
in_process_btn = InlineKeyboardButton(text='В работе', callback_data='in_process')
ready_btn = InlineKeyboardButton(text='Закрытые', callback_data='ready')
filters_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [new_btn, in_process_btn, ready_btn]
    ]
)

def lead_keyboard(lead_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text='Взять в работу',
            callback_data=f'take_{lead_id}'
        )]
    ])