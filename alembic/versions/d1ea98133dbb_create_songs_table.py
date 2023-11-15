"""create songs table

Revision ID: d1ea98133dbb
Revises: 125da73d0de2
Create Date: 2023-11-15 19:30:17.950793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1ea98133dbb'
down_revision: Union[str, None] = '125da73d0de2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
