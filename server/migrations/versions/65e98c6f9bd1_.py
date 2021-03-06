"""empty message

Revision ID: 65e98c6f9bd1
Revises: 2174e1c74a1d
Create Date: 2020-05-02 21:06:51.790291

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '65e98c6f9bd1'
down_revision = '2174e1c74a1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'visit_count',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'visit_count',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
