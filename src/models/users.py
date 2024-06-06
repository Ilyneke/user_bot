from __future__ import annotations
import datetime

from sqlalchemy import Column, String, BigInteger
from sqlalchemy.types import DateTime

from settings.db import Base


class Users(Base):
    """Схема таблицы в базе данных, хранит информацию о пользователях"""

    __tablename__ = 'users'

    id = Column(BigInteger, nullable=False, doc='Id пользователя')
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, nullable=False, default='alive', doc='Статус')
    status_updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
