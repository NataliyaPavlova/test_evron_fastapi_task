import logging

import uvicorn
from fastapi import FastAPI

from app.routes.stats import router_stats

app = FastAPI()

app.include_router(router_stats)


@app.get("/health")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    logging.basicConfig(format='{levelname:7} {message}', style='{', level=logging.INFO)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_config=None)

