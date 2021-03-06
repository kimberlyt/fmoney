"""nfirst1

Revision ID: e26453e5d56b
Revises: 726bc189f54b
Create Date: 2020-05-06 16:49:54.929491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e26453e5d56b'
down_revision = '726bc189f54b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=False,server_default='0')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
