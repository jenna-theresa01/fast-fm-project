"""create album_artists table

Revision ID: 24214c09992f
Revises: 14a7507c9a96
Create Date: 2023-11-15 19:31:16.277497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24214c09992f'
down_revision: Union[str, None] = '14a7507c9a96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
