"""empty message

Revision ID: f319cc2d2365
Revises: b732f725b913
Create Date: 2022-05-05 13:50:43.209394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f319cc2d2365'
down_revision = 'b732f725b913'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('first_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('last_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('email', sa.String(length=20), nullable=False),
                    sa.Column('contact_number', sa.String(
                        length=10), nullable=False),
                    sa.Column('credit_card', sa.String(
                        length=16), nullable=False),
                    sa.Column('billing_address', sa.String(
                        length=50), nullable=False),
                    sa.Column('password', sa.String(
                        length=10), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('contact_number'),
                    sa.UniqueConstraint('credit_card'),
                    sa.UniqueConstraint('email')
                    )
    op.create_table('equipments',
                    sa.Column('id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('year', sa.Integer(), nullable=False),
                    sa.Column('brand_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('model_name', sa.String(
                        length=20), nullable=False),
                    sa.Column('serial_number', sa.String(
                        length=20), nullable=False),
                    sa.Column('current_location', sa.String(
                        length=50), nullable=False),
                    sa.Column('daily_rate', sa.Integer(), nullable=False),
                    sa.Column('available', sa.String(
                        length=5), nullable=False),
                    sa.Column('customer_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['customer_id'], ['customers.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('serial_number')
                    )
    op.create_table('requests',
                    sa.Column('customer_id', sa.Integer(), nullable=False),
                    sa.Column('equipment_id', sa.Integer(), nullable=False),
                    sa.Column('first name', sa.String(), nullable=False),
                    sa.Column('request_location', sa.String(
                        length=50), nullable=False),
                    sa.Column('delivery_date', sa.String(
                        length=10), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['customer_id'], ['customers.id'], ),
                    sa.ForeignKeyConstraint(
                        ['equipment_id'], ['equipments.id'], ),
                    sa.PrimaryKeyConstraint('customer_id', 'equipment_id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    op.drop_table('equipments')
    op.drop_table('customers')
    # ### end Alembic commands ###