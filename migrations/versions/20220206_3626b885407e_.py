"""empty message

Revision ID: 3626b885407e
Revises: f319cc2d2365
Create Date: 2022-02-06 12:23:12.464283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3626b885407e'
down_revision = 'f319cc2d2365'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'drivers', ['credit_card'])
    op.create_unique_constraint(None, 'drivers', ['drivers_license'])
    op.create_unique_constraint(None, 'drivers', ['contact_number'])
    op.create_unique_constraint(None, 'drivers', ['email'])
    op.drop_column('drivers', 'available')
    op.drop_column('drivers', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drivers', sa.Column('id', sa.INTEGER(),
                  autoincrement=True, nullable=False))
    op.add_column('drivers', sa.Column('available', sa.TEXT(),
                  autoincrement=False, nullable=False))
    op.drop_constraint(None, 'drivers', type_='unique')
    op.drop_constraint(None, 'drivers', type_='unique')
    op.drop_constraint(None, 'drivers', type_='unique')
    op.drop_constraint(None, 'drivers', type_='unique')
    op.drop_column('drivers', 'id')
    # ### end Alembic commands ###
