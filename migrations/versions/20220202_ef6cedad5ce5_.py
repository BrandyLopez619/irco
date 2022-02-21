"""empty message

Revision ID: ef6cedad5ce5
Revises: f4d8c442a318
Create Date: 2022-02-02 16:11:51.734315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef6cedad5ce5'
down_revision = 'f4d8c442a318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('brand_name', sa.String(length=20), nullable=False),
    sa.Column('model_name', sa.String(length=20), nullable=False),
    sa.Column('serial_number', sa.String(length=20), nullable=False),
    sa.Column('current_location', sa.String(length=50), nullable=False),
    sa.Column('daily_rate', sa.Integer(), nullable=False),
    sa.Column('available', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brand_name'),
    sa.UniqueConstraint('current_location'),
    sa.UniqueConstraint('daily_rate'),
    sa.UniqueConstraint('model_name'),
    sa.UniqueConstraint('serial_number'),
    sa.UniqueConstraint('year')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipments')
    # ### end Alembic commands ###