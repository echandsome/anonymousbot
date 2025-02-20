import aiosqlite
import time

from anonymousbot import utils
from anonymousbot import config


async def run_query(query, *params, read=False, one=False):
    async with aiosqlite.connect(config.DB_PATH) as db:
        async with db.execute(query, params) as cursor:
            await db.commit()
            if read:
                if not one:
                    return await cursor.fetchall()
                else:
                    return await cursor.fetchone()


async def create_db():
    query = "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, last_activity INTEGER)"
    await run_query(query)


async def add_user_db(user_id, int_time):
    # try to update or ignore
    query = "UPDATE OR IGNORE users SET last_activity = ? WHERE user_id = ?"
    await run_query(query, int_time, user_id)
    # try to add or ignore
    query = "INSERT OR IGNORE INTO users(user_id, last_activity) VALUES (?, ?)"
    await run_query(query, user_id, int_time)


async def stats_text():
    query = "SELECT count(user_id) FROM users"
    total = (await run_query(query, read=True, one=True))[0]

    interval24h = time.time() - 60*60*24
    query = "SELECT count(user_id) FROM users WHERE last_activity > ?"
    last24h = (await run_query(query, interval24h, read=True, one=True))[0]

    interval7d = time.time() - 60*60*24*7
    query = "SELECT count(user_id) FROM users WHERE last_activity > ?"
    last7d = (await run_query(query, interval7d, read=True, one=True))[0]

    text = "<b>Total users:</b> {0}\n<b>Last7days:</b> {1}\n<b>Last24h:</b> {2}"
    text = text.format(utils.sep(total), utils.sep(last7d), utils.sep(last24h))
    return text
