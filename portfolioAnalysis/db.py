from sqlmodel import create_engine, SQLModel
from __init__ import __resources_path__

sql_engine = create_engine(
    f"sqlite:///{__resources_path__ / 'portfolio.db'}")


def init_db():
    SQLModel.metadata.create_all(sql_engine)
