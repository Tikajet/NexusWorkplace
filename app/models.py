from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class WorkStatus(Base):
    __tablename__ = "work_status"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)  # Ex: "Online", "Em pausa", "Em atendimento"
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)