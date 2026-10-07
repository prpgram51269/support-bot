import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
PROXY = os.getenv('PROXY')
DB_PATH = os.getenv('DB_PATH', 'users.db')

ADMIN_IDS = {
    int(x) for x in os.getenv('ADMIN_IDS', '').split(',') if x.strip()
}
MANAGER_IDS = {
    int(x) for x in os.getenv('MANAGER_IDS', '').split(',') if x.strip()
}