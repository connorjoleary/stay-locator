from pydantic import (
    PostgresDsn,
    computed_field,
)
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


class DBConfig:
    POSTGRES_SERVER: str = "db"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


db_config = DBConfig()
engine = create_engine(str(db_config.SQLALCHEMY_DATABASE_URI))

db = scoped_session(sessionmaker(bind=engine))


query_rows = db.execute(text("SELECT * FROM anyTableName")).fetchall()
for register in query_rows:
    print(f"{register.col_1_name}, {register.col_2_name}, ..., {register.col_n_name}")
