from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base

class User(Base):
    _tablename_ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Transaction(Base):
    _tablename_ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    type = Column(String)  # 'customer' or 'supplier'

class Ledger(Base):
    _tablename_ = "ledgers"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_money = Column(Float)

class Report(Base):
    _tablename_ = "reports"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    detail = Column(String)