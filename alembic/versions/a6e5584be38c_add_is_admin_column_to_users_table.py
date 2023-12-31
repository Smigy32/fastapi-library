"""Add is_admin column to users table

Revision ID: a6e5584be38c
Revises: fe811b7f17d9
Create Date: 2023-06-22 00:52:33.141613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6e5584be38c'
down_revision = 'fe811b7f17d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###
