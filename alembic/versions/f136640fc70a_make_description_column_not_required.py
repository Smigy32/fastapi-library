"""Make description column not required

Revision ID: f136640fc70a
Revises: 3cacf813acc6
Create Date: 2023-11-07 15:17:03.915890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f136640fc70a'
down_revision = '3cacf813acc6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('books', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###