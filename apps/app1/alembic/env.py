import os
import sys

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(project_root)

# Confirm that the root path is added correctly (optional)
print("Project Root Path:", project_root)
print("sys.path:", sys.path)
# Add the project root directory to the Python path
from alembic import context
from sqlalchemy import create_engine
from core.db.base import Base


config = context.configure
engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/monorepo")
target_metadata = Base.metadata


def run_migrations_offline():
    context.configure(
        url=engine.url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    with engine.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
