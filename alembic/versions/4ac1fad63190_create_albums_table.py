"""create albums table

Revision ID: 4ac1fad63190
Revises: 46a679ec130f
Create Date: 2023-11-15 19:29:57.831859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ac1fad63190'
down_revision: Union[str, None] = '46a679ec130f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
