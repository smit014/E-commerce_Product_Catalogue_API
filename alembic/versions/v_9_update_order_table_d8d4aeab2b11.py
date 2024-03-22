"""v 9 update order table

Revision ID: d8d4aeab2b11
Revises: 15a4e4ae92cf
Create Date: 2024-03-22 15:48:17.214638

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8d4aeab2b11'
down_revision: Union[str, None] = '15a4e4ae92cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('cart_id', sa.String(), nullable=True))
    op.create_foreign_key(None, 'orders', 'carts', ['cart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_column('orders', 'cart_id')
    # ### end Alembic commands ###
