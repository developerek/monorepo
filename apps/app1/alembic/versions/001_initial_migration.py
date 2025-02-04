# alembic/versions/001_initial_migration.py


"""add_column_to_table

Revision ID: 12345abcd678
Revises: abcdefgh1234
Create Date: 2025-02-03 15:00:00

"""
import sqlalchemy as sa
# Import the necessary Alembic methods
from alembic import op

# Declare the revision and down_revision variables
revision = '12345abcd679'  # Unique revision ID for this migration
down_revision = None


# branch_labels = None  # Optional, can specify multiple branches for migrations
# depends_on = None  # Optional, specify dependencies on other migrations

def upgrade():
    op.create_table(
        'ledger_entries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('operation',
                  sa.Enum('DAILY_REWARD', 'SIGNUP_CREDIT', 'CREDIT_SPEND', 'CREDIT_ADD', name='ledgeroperation'),
                  nullable=False),
        sa.Column('amount', sa.Integer, nullable=False),
        sa.Column('nonce', sa.String, nullable=False),
        sa.Column('owner_id', sa.String, nullable=False),
        sa.Column('created_on', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('ledger_entries')
