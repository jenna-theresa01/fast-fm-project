"""create playlists table

Revision ID: 125da73d0de2
Revises: 4ac1fad63190
Create Date: 2023-11-15 19:30:07.461134

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '125da73d0de2'
down_revision: Union[str, None] = '4ac1fad63190'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
