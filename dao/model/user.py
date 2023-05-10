from pydantic import BaseModel, Field
from sqlalchemy import MetaData, Integer, Table, Column, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

users = Table(
    'User',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('',),
    Column('',),
    Column('',),
)


class User(BaseModel):
    name: str
    fio: str
    phone: int
    email: str
