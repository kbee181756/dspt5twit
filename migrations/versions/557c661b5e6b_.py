"""empty message

Revision ID: 557c661b5e6b
Revises: 
Create Date: 2020-06-09 11:50:22.888929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557c661b5e6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('author_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###