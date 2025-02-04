import sys
import os
import httpx

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(project_root)

from fastapi.testclient import TestClient

from apps.app1.src.main import app

client = TestClient(app)


def test_get_balance():
    response = client.get("/api/v1/ledger/user123")
    assert response.status_code == 200
    assert "balance" in response.json()


def test_add_ledger_entry():
    response = client.post("/api/v1/ledger", json={
        "owner_id": "user123",
        "operation": "DAILY_REWARD",
        "amount": 1,
        "nonce": "abc123"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Ledger entry added successfully"}
