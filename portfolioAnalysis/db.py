from sqlmodel import create_engine, SQLModel
from portfolioAnalysis import __resources_path__

sql_engine = create_engine(
    f"sqlite:///{'portfolio.db'}")


def init_db():
    SQLModel.metadata.create_all(sql_engine)
