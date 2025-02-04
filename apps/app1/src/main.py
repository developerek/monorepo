import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(project_root)

# Confirm that the root path is added correctly (optional)


# Now you can import from 'core' or other modules
from fastapi import FastAPI
from core.db.session import SessionLocal  # Assuming 'core' is a folder in the project root
from core.db.base import Base
from apps.app1.src.api.ledgers.routes import router as ledger_router

app = FastAPI()
app.include_router(ledger_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to App1"}
