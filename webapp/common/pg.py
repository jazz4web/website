import asyncpg


async def get_conn(config):
    user, db = config.get('USER', default=None), config.get('DB', default=None)
    if user and db:
        conn = await asyncpg.connect(user=user, database=db)
    else:
        conn = await asyncpg.connect(config.get('DSN'))
    return conn
