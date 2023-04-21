from pydantic import BaseModel, Field
from sqlalchemy import MetaData, Integer, Table, Column, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON),
    Column('',),
    Column('',),
    Column('',),
)

users = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON),
    Column('',),
    Column('',),
    Column('',),
)


class Company(BaseModel):
    name: str
    fio: str
    inn: int
    phone: int
    email: str
    role: str
