from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel, create_engine
from sqlalchemy import Column,BigInteger

class Channel(SQLModel, table=True):
    id              : Optional[int]     = Field(default=None, primary_key=True)
    name            : str               = Field(default=None)
    channel_id      : int               = Field(sa_column=Column(BigInteger))
    is_active       : Optional[bool]    = True
    created_date    : datetime          = Field(default_factory=datetime.utcnow,nullable=False)
