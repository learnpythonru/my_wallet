"""add user.mobile column

Revision ID: 203507278683
Revises: df8160c06bce
Create Date: 2022-11-07 12:13:24.207946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '203507278683'
down_revision = 'df8160c06bce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('mobile', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'mobile')
    # ### end Alembic commands ###