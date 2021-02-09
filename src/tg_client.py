import asyncio
import logging
import telebot
from telethon.sync import events
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from src.config import API_ID, API_HASH, SESSION_STRING, EZWORK_BOT_TOKEN
from src.models import Message
from src.utils import parse_message, get_message_without_message_id, add_message_to_db

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

CHATS_LIST = [-463340134, -474873064]

message_from_ezwork = {
    'chat_id': -463340134,
    'user_id': 558692780,
    'message_id': 0,
    'message_text': 'проверка'
}


async def send_message_to_telegram(message_from_db):
    tb = telebot.TeleBot(EZWORK_BOT_TOKEN)
    tb.config['api_key'] = EZWORK_BOT_TOKEN
    tb.send_message(-463340134, message_from_db)


async def read_db():
    while True:
        message_from_db = get_message_without_message_id()
        print(message_from_db.message_text)
        tb = telebot.TeleBot(EZWORK_BOT_TOKEN)
        await send_message_to_telegram(message_from_db.message_text)
        await asyncio.sleep(4)


async def client_handlers():
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        @client.on(events.NewMessage(chats=CHATS_LIST))
        async def handler_new_message(event):
            """ Хендлер: запись в БД входящего сообщения из ТГ """
            try:
                print(event.message.message)
                add_message_to_db(Message(**parse_message(event)))
            except Exception as ex:
                print(ex)


async def main():
    task1 = await asyncio.create_task(read_db())
    task2 = await asyncio.create_task(client_handlers())
    await asyncio.gather(task2, task1)


if __name__ == '__main__':
    asyncio.run(main())
