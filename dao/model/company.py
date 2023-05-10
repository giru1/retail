from pydantic import BaseModel, Field
from sqlalchemy import MetaData, Integer, Table, Column, String, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

company = Table(
    'Company',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('fio', String, nullable=True),
    Column('inn', Integer, nullable=True),
    Column('phone', Integer, nullable=True),
    Column('email', Integer, nullable=True),
)


class Company(BaseModel):
    id: int
    name: str
    fio: str
    inn: int = Field(max_length=15)
    phone: int
    email: str
