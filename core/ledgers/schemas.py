# monorepo/core/ledgers/schemas.py
from enum import Enum

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseLedgerOperation(str, Enum):
    DAILY_REWARD = "DAILY_REWARD"
    SIGNUP_CREDIT = "SIGNUP_CREDIT"
    CREDIT_SPEND = "CREDIT_SPEND"
    CREDIT_ADD = "CREDIT_ADD"


class LedgerEntry(Base):
    __tablename__ = 'ledger_entries'
    id = Column(Integer, primary_key=True)
    operation = Column(SQLEnum(BaseLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False)


class LedgerOperationRequest(BaseModel):
    owner_id: str
    operation: BaseLedgerOperation
    amount: int
    nonce: str


class LedgerBalanceResponse(BaseModel):
    owner_id: str
    balance: int
