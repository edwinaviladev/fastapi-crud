import redis.asyncio as redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

async def init_cache():
    redis_client = redis.Redis(host="localhost", port=6379)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")