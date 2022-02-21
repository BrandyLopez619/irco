"""empty message

Revision ID: 3f6f4d8bedbe
Revises: 4b6adc425fcb
Create Date: 2022-02-04 22:22:37.036062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6f4d8bedbe'
down_revision = '4b6adc425fcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('requests', 'request_location',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('requests', 'delivery_date',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('requests', 'delivery_date',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('requests', 'request_location',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
