"""create album_songs table

Revision ID: 14a7507c9a96
Revises: ff6a75626366
Create Date: 2023-11-15 19:31:06.840494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14a7507c9a96'
down_revision: Union[str, None] = 'ff6a75626366'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
