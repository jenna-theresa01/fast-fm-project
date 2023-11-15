"""create playlist_songs table

Revision ID: ff6a75626366
Revises: 12ef2bcc3b85
Create Date: 2023-11-15 19:30:51.050172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff6a75626366'
down_revision: Union[str, None] = '12ef2bcc3b85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
