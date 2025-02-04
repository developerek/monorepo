# monorepo/core/ledgers/models.py
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base

from core.ledgers.schemas import BaseLedgerOperation

Base = declarative_base()


class LedgerEntry(Base):
    __tablename__ = 'ledger_entries'
    __table_args__ = {'schema': 'monorepo'}
    id = Column(Integer, primary_key=True)
    operation = Column(SQLEnum(BaseLedgerOperation), nullable=False)
    amount = Column(Integer, nullable=False)
    nonce = Column(String, nullable=False)
    owner_id = Column(String, nullable=False)
    created_on = Column(DateTime, nullable=False)
