from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import Column,BigInteger

sqlite_file_name = "channels.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)