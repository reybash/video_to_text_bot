import asyncio
from aiomysql import DictCursor
import aiomysql
from config import DATABASE_CONFIG

loop = asyncio.get_event_loop()


async def connect():
    return await aiomysql.create_pool(
        host=DATABASE_CONFIG["host"],
        port=DATABASE_CONFIG["port"],
        user=DATABASE_CONFIG["user"],
        password=DATABASE_CONFIG["password"],
        db=DATABASE_CONFIG["db"],
        autocommit=True,
        pool_recycle=100,
        loop=loop,
    )


db_connect = loop.run_until_complete(connect())


async def insert(sql, data):
    async with db_connect.acquire() as conn:
        async with conn.cursor(DictCursor) as cur:
            await cur.execute(sql, data)
