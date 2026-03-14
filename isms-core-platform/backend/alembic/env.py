"""Alembic migration environment.

init_db.sql creates the full schema via Docker initdb.
Alembic stamps head to inherit that state.
Future schema changes go through alembic revision --autogenerate.
"""

import os

from alembic import context
from sqlalchemy import engine_from_config, pool

# Import all models so Base.metadata has the full picture
from src.database.base import Base
from src.domain import *  # noqa: F401, F403

config = context.config

# Override sqlalchemy.url from environment if set
db_url = os.environ.get("DATABASE_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
