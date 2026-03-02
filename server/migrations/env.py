import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

from sqlmodel import SQLModel

from models import Subscription 

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Link SQLModel's metadata to Alembic
target_metadata = SQLModel.metadata

# --- DATABASE URL CONFIGURATION ---
# We manually set the sqlalchemy.url here so it overrides alembic.ini
# Note: Use psycopg2 (sync) for migrations even if the app is async.
DATABASE_URL = "postgresql+psycopg2://postgres.morrapsnmmomdiogwmun:NXT2h92BJ0OqcBrq@aws-0-us-west-2.pooler.supabase.com:6543/postgres"
config.set_main_option("sqlalchemy.url", DATABASE_URL)
# ----------------------------------

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # This helper creates the engine using the URL we injected above
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            # compare_type=True helps detect changes in column types (e.g. String to Text)
            compare_type=True 
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()