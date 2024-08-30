"""First migration

Revision ID: 32cf4a968ce2
Revises: 
Create Date: 2024-08-30 13:43:22.051381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32cf4a968ce2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)

    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_notes_user_id_user'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_notes_description'), ['description'], unique=False)
        batch_op.create_index(batch_op.f('ix_notes_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_notes_name'), ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_notes_name'))
        batch_op.drop_index(batch_op.f('ix_notes_id'))
        batch_op.drop_index(batch_op.f('ix_notes_description'))

    op.drop_table('notes')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    # ### end Alembic commands ###