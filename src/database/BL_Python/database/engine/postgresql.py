from typing import Any, Callable, Union

from BL_Python.database.config import DatabaseConnectArgsConfig
from BL_Python.database.types import MetaBase
from sqlalchemy import create_engine
from sqlalchemy.orm.scoping import ScopedSession
from sqlalchemy.orm.session import sessionmaker


class PostgreSQLScopedSession(ScopedSession):
    @staticmethod
    def create(
        connection_string: str,
        echo: bool = False,
        execution_options: dict[str, Any] | None = None,
        connect_args: DatabaseConnectArgsConfig | None = None,
        bases: list[type[MetaBase]] | None = None,
    ) -> "PostgreSQLScopedSession":
        engine = create_engine(
            connection_string,
            echo=echo,
            execution_options=execution_options or {},
            connect_args=connect_args.model_dump() if connect_args is not None else {},
        )

        if bases:
            # This renames all tables to undo any renaming that previously happened
            # from, e.g., our SQLite engine.
            for metadata_base in bases:
                metadata_base.metadata.reflect(bind=engine)
                for table_subclass in metadata_base.__subclasses__():
                    schema: str | None = None
                    if hasattr(metadata_base, "__table_args__") and isinstance(
                        metadata_base.__table_args__, dict
                    ):
                        schema = metadata_base.__table_args__.get("schema")

                    if schema:
                        table_name: list[str] = table_subclass.__tablename__.split(".")
                        # Trim all prepended schema names
                        while table_name[0] == schema:
                            table_name = table_name[1:]

                        table_subclass.__tablename__ = table_name[0]

                        for table in metadata_base.metadata.sorted_tables:
                            table_name = table.name.split(".")
                            while table_name[0] == table.schema:
                                table_name = table_name[1:]

                            table.name = ".".join(table_name)
                            table.fullname = f"{table.schema}.{table.name}"

        return PostgreSQLScopedSession(
            sessionmaker(autocommit=False, autoflush=False, bind=engine)
        )

    def __init__(
        self,
        session_factory: Union[Callable[..., Any], "sessionmaker[Any]"],
        scopefunc: Any = None,
    ) -> None:
        super().__init__(session_factory, scopefunc)
