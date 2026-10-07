# Support Bot 🎫

Telegram-бот для службы поддержки с ролями.

## Функции

- ✅ Регистрация клиентов
- ✅ Оставить заявку
- ✅ Менеджер видит новые заявки
- ✅ Менеджер берёт заявку в работу
- ✅ Переписка менеджер ↔ клиент
- ✅ Роли: клиент / менеджер / админ
- ✅ Статистика заявок

## Стек

- Python 3.11+
- Aiogram 3
- SQLite
- aiohttp

## Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/prpgram51269/support-bot.git
   cd support-bot
   ```

2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создай `.env`:
   ```
   BOT_TOKEN=твой_токен
   PROXY=твой_прокси
   ADMIN_IDS=твой_id
   MANAGER_IDS=твой_id
   DB_PATH=users.db
   ```

4. Запусти:
   ```bash
   python main.py
   ```

## Структура

```
support_bot/
├── main.py
├── config.py
├── database.py
├── keyboards.py
├── states.py
├── filters.py
├── handlers/
│   ├── start.py
│   ├── client.py
│   ├── manager.py
│   └── admin.py
└── requirements.txt
```

## Роли

| Роль | Что может |
|---|---|
| **Клиент** | Оставить заявку, смотреть статус |
| **Менеджер** | Видеть заявки, брать в работу, отвечать |
| **Админ** | Всё + статистика, фильтры |

## Автор

[prpgram51269](https://github.com/prpgram51269)