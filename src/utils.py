import time

from db import session
from models import Message


def parse_message(event):
    """
    Преобразование сообщения из формата Телеграм в словарь
    :param event:
    :return dict:
    """
    return dict(
        chat_id=event.message.chat_id,
        user_id=event.from_id.user_id,
        message_id=event.message.id,
        # message_date=event.message.date,
        message_text=event.message.message,
        # publish_in_ezwork = publish_in_ezwork
    )


def add_message_to_db(message):
    """ Запись сообщений из Телеграм в БД """
    session.add(message)
    session.commit()
    print('write in db')


def get_message_without_message_id():
    """ Список сообщений не опубликованных в Телеграм, message_id=0 """
    return session.query(Message).filter(Message.message_id == 0).first()


def message_id_update(message_id):
    """ Обновление (присвоение message_id из ТГ,  вместо 0) сообщениям опубликованных в Телеграм """
    session.query(Message).filter_by(message_id=0).update({"message_id": message_id})
    session.commit()
