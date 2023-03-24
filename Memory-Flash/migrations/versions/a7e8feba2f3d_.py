"""empty message

Revision ID: a7e8feba2f3d
Revises: 
Create Date: 2022-05-17 11:31:57.338579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7e8feba2f3d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testing_migrate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('test_one', sa.Integer(), nullable=True),
    sa.Column('test_two', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testing_migrate')
    # ### end Alembic commands ###
