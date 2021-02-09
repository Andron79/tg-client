from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from src.config import (API_ID, API_HASH)


# Авторизация и печать ключа сессии
with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
    print(client.get_me().stringify())
# print(API_ID, API_HASH)
