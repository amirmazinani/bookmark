"""empty message

Revision ID: 416e0a6f19e5
Revises: 2bbc69e73148
Create Date: 2020-04-24 21:19:01.027220

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '416e0a6f19e5'
down_revision = '2bbc69e73148'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=512),
               nullable=True)
    op.alter_column('users', 'phone',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=512),
               nullable=False)
    # ### end Alembic commands ###
