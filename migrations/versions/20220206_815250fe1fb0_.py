"""empty message

Revision ID: 815250fe1fb0
Revises: 3626b885407e
Create Date: 2022-02-06 12:58:00.159031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '815250fe1fb0'
down_revision = '3626b885407e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requests',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.Column('request_location', sa.String(length=50), nullable=False),
    sa.Column('delivery_date', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.id'], ),
    sa.PrimaryKeyConstraint('customer_id', 'equipment_id')
    )
    op.add_column('drivers', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.add_column('drivers', sa.Column('billing_address', sa.String(length=50), nullable=False))
    op.add_column('drivers', sa.Column('password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drivers', 'password')
    op.drop_column('drivers', 'billing_address')
    op.drop_column('drivers', 'id')
    op.drop_table('requests')
    # ### end Alembic commands ###
