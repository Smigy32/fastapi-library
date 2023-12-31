"""Add Books and Authors

Revision ID: 66a3de137daa
Revises: b53da2711cfd
Create Date: 2023-06-21 13:51:24.712320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66a3de137daa'
down_revision = 'b53da2711cfd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_author_association',
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_author_association')
    op.drop_table('books')
    op.drop_table('authors')
    # ### end Alembic commands ###
