"""test::Initial migration.

Revision ID: 65b955e65c7a
Revises: 
Create Date: 2020-04-14 12:18:16.814927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b955e65c7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=512), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=512), nullable=False),
    sa.Column('phone', sa.String(length=32), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('visit_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###