import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from src.config import SQLALCHEMY_DATABASE_URL


# db settings
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres_user:postgres_pass@localhost:5432/postgres_db'
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()

from src.models import *  # noqa

