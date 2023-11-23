"""Added bookings, hotels, rooms, users(3)

Revision ID: 354d14da4c6c
Revises: d308de05e564
Create Date: 2023-11-07 21:11:44.563743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '354d14da4c6c'
down_revision: Union[str, None] = 'd308de05e564'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('rooms', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('rooms', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('rooms', 'price',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('rooms', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('rooms', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('rooms', 'price',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('rooms', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('rooms', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('rooms', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
