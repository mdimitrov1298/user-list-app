"""Update phone column type

Revision ID: c96b814c2037
Revises: d99e1d6629e1
Create Date: 2024-09-12 06:52:54.729973

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'c96b814c2037'
down_revision = 'd99e1d6629e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'phone',
               existing_type=sa.INTEGER(),
               type_=sqlmodel.sql.sqltypes.AutoString(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'phone',
               existing_type=sqlmodel.sql.sqltypes.AutoString(length=255),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
