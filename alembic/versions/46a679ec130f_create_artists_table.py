"""create artists table

Revision ID: 46a679ec130f
Revises: 1facbd6f61e6
Create Date: 2023-11-15 19:29:47.631664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46a679ec130f'
down_revision: Union[str, None] = '1facbd6f61e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
