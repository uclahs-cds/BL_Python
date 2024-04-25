from configparser import ConfigParser
from pathlib import Path
from typing import cast

from alembic import context
from alembic.command import downgrade, upgrade
from alembic.config import Config as AlembicConfig
from BL_Python.database.config import Config
from BL_Python.database.dependency_injection import get_database_config_container
from BL_Python.database.migrations.alembic.env_setup import AlembicEnvSetup
from BL_Python.database.types import MetaBase
from BL_Python.programming.config import ConfigBuilder, load_config
from sqlalchemy.engine import Engine


def get_migration_config(config_filename: Path | None = None):
    if config_filename is None:
        config_filename = Path("config.toml")

    config_type = ConfigBuilder[Config]().with_root_config(Config).build()
    return load_config(config_type, config_filename)


def run_migrations_with_config(bases: list[MetaBase], config: Config):
    ioc_container = get_database_config_container(config)

    alembic_env = ioc_container.create_object(AlembicEnvSetup)

    if context.is_offline_mode():
        alembic_env.run_migrations_offline(bases)
    else:
        alembic_env.run_migrations_online(bases)


def run_migrations(bases: list[MetaBase], config_filename: Path | None = None):
    config = get_migration_config(config_filename)
    run_migrations_with_config(bases, config)


def set_up_database(
    engine: Engine,
    down_revision: str | None = "base",
    up_revision: str | None = "head",
    config_filename: str = "alembic.ini",
) -> Engine._trans_ctx:
    alembic_config = AlembicConfig()
    alembic_config.set_main_option("config_file_name", config_filename)
    _ = cast(ConfigParser, alembic_config.file_config).read(config_filename)

    # Maintain the connection so Alembic does not wipe out the in-memory database
    # when using SQLite in-memory connections
    # https://alembic.sqlalchemy.org/en/latest/cookbook.html#sharing-a-connection-across-one-or-more-programmatic-migration-commands
    connection: Engine._trans_ctx = engine.begin()
    alembic_config.attributes["connection"] = connection.conn  # pyright: ignore[reportIndexIssue]

    if down_revision is not None:
        downgrade(alembic_config, down_revision, False)

    if up_revision is not None:
        upgrade(alembic_config, up_revision, False)

    return connection
