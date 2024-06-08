import logging
import time

from app.dto.user import UserStats
from app.services.client_service import ClientService
from app.settings import settings


class UserService:

    def __init__(self):
        self.threshold = 0
        self.client_service = ClientService()

    async def is_filter_passed(self, user: UserStats) -> bool:
        return True if user.stats < self.threshold else False

    @staticmethod
    async def get_all() -> list[int]:
        # to do get from DB
        # to do generators
        time.sleep(1)
        logging.info("get all users")
        return [i for i in range(10)]

    async def get_stats(
            self,
            threshold: int,
            batch_size: int = settings.batch_size
    ) -> list[UserStats]:
        result = []
        self.threshold = threshold
        users_ids = await self.get_all()
        users_with_stat = await self.client_service.get_stats(users_ids)
        for user in users_with_stat:
            if await self.is_filter_passed(user):
                result.append(user)

        return result

