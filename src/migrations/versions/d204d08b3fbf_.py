"""empty message

Revision ID: d204d08b3fbf
Revises: 
Create Date: 2024-03-08 20:01:06.103092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd204d08b3fbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sub_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('sub_cate_name', sa.String(length=100), nullable=False),
    sa.Column('cost', sa.Numeric(scale=2), nullable=True),
    sa.Column('cate_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cate_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sub_category')
    # ### end Alembic commands ###