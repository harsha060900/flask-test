"""empty message

Revision ID: 0c0a243a03cc
Revises: bb09475a8d7b
Create Date: 2024-03-05 17:39:06.371668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c0a243a03cc'
down_revision = 'bb09475a8d7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
        batch_op.drop_constraint('category_cate_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('category', schema=None) as batch_op:
        batch_op.create_unique_constraint('category_cate_name_key', ['cate_name'])
        batch_op.alter_column('id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False,
               autoincrement=True)

    # ### end Alembic commands ###
