from pydantic import BaseModel


class User(BaseModel):
    user_id: int


class UserStats(User):
    stats: int

