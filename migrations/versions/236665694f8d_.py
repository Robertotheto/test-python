"""empty message

Revision ID: 236665694f8d
Revises: 33466447387b
Create Date: 2024-05-20 00:53:30.356584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '236665694f8d'
down_revision = '33466447387b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token_block_list',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('jti', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token_block_list')
    # ### end Alembic commands ###
