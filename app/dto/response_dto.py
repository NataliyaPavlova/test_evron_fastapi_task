from pydantic import BaseModel


class UserStats(BaseModel):
    user_id: int
    stats: int


class UsersStatsResponseDTO(BaseModel):
    result: list[UserStats]
