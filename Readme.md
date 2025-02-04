# Shared Ledger System

This project is a **shared ledger system** designed for a monorepo containing multiple applications. It focuses on **code reuse** and **type safety**, allowing each application to track user credits through a shared ledger system while supporting application-specific operations.

---

## Features

- **Core Ledger System**: Shared ledger functionality for tracking user credits.
- **Application-Specific Extensions**: Each application can extend the core ledger system with its own operations.
- **Type Safety**: Enforced through Python's `Enum` and type hints.
- **REST API**: Built with **FastAPI** for managing ledger entries and balances.
- **Database**: Uses **PostgreSQL** for persistent storage.
- **Containerization**: Dockerized for consistent environments.
- **Migrations**: Uses **Alembic** for database schema migrations.

---

## Technologies

- **Python ≥ 3.10**
- **FastAPI**
- **SQLAlchemy ≥ 2.0.0**
- **Pydantic**
- **Alembic**
- **PostgreSQL**
- **Docker**
- **Docker Compose**

---

## Project Structure


---

## Getting Started

### Prerequisites

- **Python 3.10** or higher
- **Docker** and **Docker Compose**
- **PostgreSQL** (if not using Docker)

---

### Installation


