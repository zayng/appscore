"""initial migrate

Revision ID: ba65c26a43ee
Revises: None
Create Date: 2016-10-20 18:13:13.648923

"""

# revision identifiers, used by Alembic.
revision = 'ba65c26a43ee'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=80), nullable=True),
                    sa.Column('email', sa.String(length=80), nullable=True),
                    sa.Column('password', sa.String(length=128), nullable=True),
                    sa.Column('sex', sa.Integer(), nullable=True),
                    sa.Column('member_since', sa.DateTime(), nullable=True),
                    sa.Column('ts', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    op.create_index(op.f('ix_user_member_since'), 'user', ['member_since'], unique=False)
    op.create_index(op.f('ix_user_ts'), 'user', ['ts'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_ts'), table_name='user')
    op.drop_index(op.f('ix_user_member_since'), table_name='user')
    op.drop_table('user')
    ### end Alembic commands ###
