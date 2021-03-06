"""empty message

Revision ID: 92a0bb1d0313
Revises: 0536c3ee39db
Create Date: 2020-03-05 19:13:24.675223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92a0bb1d0313'
down_revision = '0536c3ee39db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Venue_Genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(length=120), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Genres')
    # ### end Alembic commands ###
