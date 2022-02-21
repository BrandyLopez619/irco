"""empty message

Revision ID: b732f725b913
Revises: 3f6f4d8bedbe
Create Date: 2022-02-05 10:49:32.740716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b732f725b913'
down_revision = '3f6f4d8bedbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('password', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'password')
    # ### end Alembic commands ###
