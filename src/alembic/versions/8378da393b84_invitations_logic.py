"""Invitations logic

Revision ID: 8378da393b84
Revises: 2e40e779fbd1
Create Date: 2026-04-26 18:38:28.087768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8378da393b84'
down_revision: Union[str, Sequence[str], None] = '2e40e779fbd1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
