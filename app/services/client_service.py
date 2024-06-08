import asyncio
import logging
import random
import time
from asyncio import Task, create_task

import aiohttp

from app.dto.user import UserStats
from app.settings import settings


class ClientService:

    def __init__(self):
        self.base_url = settings.client_base_url
        self.headers = settings.client_headers

    @staticmethod
    async def connect():
        time.sleep(2)

    async def get_stats_one(self, session: aiohttp.ClientSession, uid: int) -> UserStats:
        time.sleep(1)
        # url = f'{settings.client_base_url}{settings.client_path % uid}'
        # try:
        #     response: aiohttp.ClientResponse = await session.get(url=url)
        #     if response.ok:
        #         response = await response.json()
        # except Exception:
        #     raise
        logging.info("getting stats for user %s", uid)
        return UserStats(user_id=uid, stats=random.randrange(0, 100))

    async def get_stats(self, uids: list[int]) -> list[UserStats]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks: list[Task] = []
            for uid in uids:
                tasks.append(create_task(self.get_stats_one(session=session, uid=uid)))
            if tasks:
                results_task = await self.start_tasks(tasks=tasks)
                return results_task
        raise Exception

    @staticmethod
    async def start_tasks(tasks: list[Task]) -> list:
        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
        results_tasks = []
        for done_task in done:
            if not done_task.exception():
                results_tasks.append(done_task.result())

        for pending_task in pending:
            pending_task.cancel()
        return results_tasks

