"""empty message

Revision ID: a3b62d01c5a0
Revises: 416e0a6f19e5
Create Date: 2020-04-24 23:59:50.473925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3b62d01c5a0'
down_revision = '416e0a6f19e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('salt', sa.String(length=128), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'salt')
    # ### end Alembic commands ###
