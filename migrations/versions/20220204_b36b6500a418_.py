"""empty message

Revision ID: b36b6500a418
Revises: 8d035aef6bd5
Create Date: 2022-02-04 16:40:32.947165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36b6500a418'
down_revision = '8d035aef6bd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requests',
                    sa.Column('customer_id', sa.Integer(), nullable=False),
                    sa.Column('equipment_id', sa.Integer(), nullable=False),
                    sa.Column('request_date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['customer_id'], ['customers.id'], ),
                    sa.ForeignKeyConstraint(
                        ['equipment_id'], ['equipments.id'], ),
                    sa.PrimaryKeyConstraint('customer_id', 'equipment_id')
                    )
    op.add_column('equipments', sa.Column(
        'customer_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'equipments', 'customers', [
                          'customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'equipments', type_='foreignkey')
    op.drop_column('equipments', 'customer_id')
    op.drop_table('requests')
    # ### end Alembic commands ###
