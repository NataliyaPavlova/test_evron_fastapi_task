from fastapi import APIRouter
from fastapi.params import Depends

from app.dto.response_dto import UsersStatsResponseDTO, UserStats
from app.services.user_service import UserService

router_stats = APIRouter(tags=["stats"])


@router_stats.get(
    "/users/stats",
    response_model=UsersStatsResponseDTO
)
async def users_stats(
        threshold: int,
        user_service: UserService = Depends(UserService)
):
    users = await user_service.get_stats(threshold)
    return UsersStatsResponseDTO(
        result=[
            UserStats(
              user_id=user.user_id,
              stats=user.stats
            ) for user in users]
    )
