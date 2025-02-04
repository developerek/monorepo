from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from core.db.session import get_db
from core.ledgers.operations import validate_transaction, add_ledger_entry, calculate_balance
from core.ledgers.schemas import LedgerEntry, BaseLedgerOperation
from core.ledgers.schemas import LedgerOperationRequest, LedgerBalanceResponse

router = APIRouter()

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/monorepo"
engine = create_engine(DATABASE_URL)


@router.get("/ledger/{owner_id}")
def get_balance(owner_id: str):
    with Session(engine) as session:
        entries = session.query(LedgerEntry).filter(LedgerEntry.owner_id == owner_id).all()
        balance = sum(entry.amount for entry in entries)
        return {"balance": balance}


@router.post("/ledger")
def add_ledger_entry(request: LedgerOperationRequest):
    with Session(engine) as session:
        # Check for duplicate nonce
        if session.query(LedgerEntry).filter(LedgerEntry.nonce == request.nonce).first():
            raise HTTPException(status_code=400, detail="Duplicate transaction")

        # Validate sufficient balance for CREDIT_SPEND
        if request.operation == BaseLedgerOperation.CREDIT_SPEND:
            balance = get_balance(request.owner_id)["balance"]
            if balance < request.amount:
                raise HTTPException(status_code=400, detail="Insufficient balance")

        # Create new ledger entry
        entry = LedgerEntry(
            operation=request.operation,
            amount=request.amount,
            nonce=request.nonce,
            owner_id=request.owner_id,
            created_on=datetime.now()
        )
        session.add(entry)
        session.commit()
        return {"message": "Ledger entry added successfully"}
