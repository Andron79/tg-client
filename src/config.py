from os import environ
from dotenv import load_dotenv

load_dotenv()

# Загрузка значений из переменных окружения Telegram
API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
SESSION_STRING = environ.get('SESSION_STRING')
SOURCE_CHANNEL = environ.get('SOURCE_CHANNEL')
EZWORK_BOT_TOKEN = environ.get('EZWORK_BOT_TOKEN')

# Загрузка значений из переменных окружения Postgres
DB_USER = environ.get('DB_USER', 'postgres_user')
DB_PASSWORD = environ.get('DB_PASSWORD', 'postgres_pass')
DB_NAME = environ.get('DB_NAME', 'postgres_db')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_PORT = environ.get('DB_PORT', 5432)

SQLALCHEMY_DATABASE_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
