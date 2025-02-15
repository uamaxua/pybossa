"""
Add is_private column to project and create project_to_user table

Revision ID: abc123def456
Revises: a791f9de9ac3
Create Date: 2024-02-14 10:30:00.000000
"""

revision = 'abc123def456'
down_revision = 'a791f9de9ac3'

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op


def upgrade():
    op.add_column('project',
                  sa.Column('is_private', sa.Boolean(), server_default=sa.sql.expression.false(), nullable=False))
    op.add_column('project', sa.Column('private_users_ids', postgresql.ARRAY(sa.Integer)))


def downgrade():
    op.drop_column('project', 'is_private')
    op.drop_column('project', 'private_users_ids')
