from pydantic import BaseModel, Field
from sqlalchemy import MetaData, Table, Column, String, Integer, JSON

metadate = MetaData()

roles = Table(
    "roles",
    metadate,
    Column('id', Integer, primary_key=True),
    Column('name', nullable=True),
    Column('permissions', JSON)
)


class Roles(BaseModel):
    id: int
    name: str
    fio: str
    inn: int = Field(max_length=15)
    phone: int
    email: str
