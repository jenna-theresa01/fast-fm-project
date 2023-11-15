"""create song_artists table

Revision ID: 12ef2bcc3b85
Revises: d1ea98133dbb
Create Date: 2023-11-15 19:30:38.317566

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12ef2bcc3b85'
down_revision: Union[str, None] = 'd1ea98133dbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
