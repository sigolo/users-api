from ..api.schemas import User
from .db_models import Users
from .db_engine import database
from ..utils import hashing


async def create(user: User):
    query = Users.insert().values(email=user.email, password=hashing.bcrypt(user.password))
    return await database.execute(query=query)


async def get_one(id: int):
    query = Users.select().where(id == Users.c.id)
    return await database.fetch_one(query=query)