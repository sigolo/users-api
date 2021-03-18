from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.sql import expression

metadata = MetaData()

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50)),
    Column("password", String(50)),
    Column("is_admin", Boolean, default=expression.false()),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

