from datetime import datetime

from sqlalchemy import Table, Boolean, Column, Integer, String, NVARCHAR, DATETIME, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_time
import time
from config.database import Base

class Channel(Base):
    __tablename__ = 'Channel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(50))

    account = relationship("Account", back_populates="channel")
    message = relationship("Message", back_populates="channel")

class Account(Base):
    __tablename__ = 'Account'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(50))
    ChannelId = Column(Integer, ForeignKey(Channel.id))

    channel = relationship("Channel", back_populates="account")
    message = relationship("Message", back_populates="account")

class Message(Base):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    AccountId = Column(Integer, ForeignKey(Account.id))
    ChannelId = Column(Integer, ForeignKey(Channel.id))
    Msg = Column(NVARCHAR(200))
    # Time = Column(DATETIME, default= current_time(datetime.now()))

    account = relationship("Account", back_populates="message")
    channel = relationship("Channel", back_populates="message")