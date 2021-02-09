from sqlalchemy import MetaData, Column, TIMESTAMP, DateTime, Integer, String


from src.db import Base

metadata = MetaData(schema='public')


class Message(Base):
    """
    Объект сообщение.
    """
    __tablename__ = 'message'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, default=0)
    user_id = Column(Integer, default=0)
    message_id = Column(Integer, default=0)  # Если значение 0, значит не записано в БД, после записи в БД получает ID
    # message_date = Column(DateTime)
    message_text = Column(String, nullable=False)
    # publish_in_ezwork = Column(Boolean, default=False)  # Флаг: True - опубликовано в Ezwork, False - не опубликовано

    def __init__(self, chat_id=0, user_id=0, message_id=0, message_text=''):  # message_date=0,
        self.chat_id = chat_id
        self.user_id = user_id
        self.message_id = message_id
        # self.message_date = message_date
        self.message_text = message_text
        # self.publish_in_ezwork = publish_in_ezwork

    def __repr__(self):
        return "<Message ('%s','%s', %s, %s)>" % (self.chat_id, self.user_id, self.message_id, self.message_text)
        # datetime.fromtimestamp(self.message_date))
