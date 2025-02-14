"""
Add is_restricted column to projects and create projects_to_users table

Revision ID: abc123def456
Revises: a791f9de9ac3
Create Date: 2024-02-14 10:30:00.000000
"""

# revision identifiers, used by Alembic.
revision = 'abc123def456'
down_revision = 'a791f9de9ac3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # Add is_restricted column to projects table
    op.add_column('projects', sa.Column('is_restricted', sa.Boolean(), server_default=sa.sql.expression.false(), nullable=False))

    # Create project_to_users table (many-to-many relationship)
    op.create_table(
        'projects_to_users',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint('user_id', 'project_id')
    )


def downgrade():
    # Drop project_to_users table
    op.drop_table('projects_to_users')

    # Remove is_restricted column from projects
    op.drop_column('projects', 'is_restricted')