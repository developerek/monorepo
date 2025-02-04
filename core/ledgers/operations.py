# monorepo/core/ledgers/operations.py

import datetime

from sqlalchemy.orm import Session

from core.ledgers.exceptions import InsufficientBalanceError, DuplicateTransactionError
from core.ledgers.models import LedgerEntry
from core.ledgers.schemas import LedgerOperationRequest


def validate_transaction(db: Session, request: LedgerOperationRequest):
    # Check for duplicate nonce
    if db.query(LedgerEntry).filter(LedgerEntry.nonce == request.nonce).first():
        raise DuplicateTransactionError("Duplicate transaction detected")

    # Validate sufficient balance for CREDIT_SPEND
    if request.operation == "CREDIT_SPEND":
        balance = calculate_balance(db, request.owner_id)
        if balance < request.amount:
            raise InsufficientBalanceError("Insufficient balance")


def calculate_balance(db: Session, owner_id: str) -> int:
    entries = db.query(LedgerEntry).filter(LedgerEntry.owner_id == owner_id).all()
    return sum(entry.amount for entry in entries)


def add_ledger_entry(db: Session, request: LedgerOperationRequest):
    entry = LedgerEntry(
        operation=request.operation,
        amount=request.amount,
        nonce=request.nonce,
        owner_id=request.owner_id,
        created_on=datetime.now()
    )
    db.add(entry)
    db.commit()
