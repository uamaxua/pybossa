"""
Add is_private column to project and create project_to_user table

Revision ID: abc123def456
Revises: a791f9de9ac3
Create Date: 2024-02-14 10:30:00.000000
"""

revision = 'abc123def456'
down_revision = 'a791f9de9ac3'

import sqlalchemy as sa

from alembic import op


def upgrade():
    op.add_column('project',
                  sa.Column('is_private', sa.Boolean(), server_default=sa.sql.expression.false(), nullable=False))
    op.create_table(
        'project_to_user',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(['project_id'], ['project.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('user_id', 'project_id')
    )


def downgrade():
    op.drop_table('project_to_user')
    op.drop_column('projects', 'is_restricted')
