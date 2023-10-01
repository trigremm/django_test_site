# django_app/common/caches.py
# warning this file is depenent on django cache

import redis
from common.loggers import logger
from django.core.cache import cache


def get_key_from_cache(key):
    # general logic for the key is url + params
    # add count logic
    return cache.get(key)


def set_key_to_cache(key, value, timeout=None):
    logger.debug(f"Setting {key} to cache with {timeout=}.")
    return cache.set(key, value, timeout)


def get_ttl(key):
    if cache.get(key) is None:
        return f"{key=} does not exist in cache."

    ttl = cache.ttl(key)
    if ttl is None:
        return f"{key=} exists but does not have an expiry."
    else:
        return f"TTL for {key} is {ttl} seconds."


def get_all_redis_keys():
    # Get the raw Redis client from the cache
    redis_client = cache.client.get_client()

    # Use the Redis client to get all keys
    keys = redis_client.keys("*")

    # Return the keys
    return keys


def get_redis_space():
    # Connect to your Redis server
    r = redis.Redis(host="redis-oraclus", port=6379, db=0)

    # Get memory info
    info = r.info("memory")

    memory_limit = info["maxmemory"]
    memory_limit_mb = memory_limit / (1024 * 1024)
    print(f"Memory Limit: {memory_limit_mb:.2f} MB")

    memory_used = info["used_memory"]
    memory_used_mb = memory_used / (1024 * 1024)
    print(f"Used Memory: {memory_used_mb:.2f} MB")

    memory_left = memory_limit - memory_used
    memory_left_mb = memory_left / (1024 * 1024)
    print(f"Memory left: {memory_left_mb:.2f} MB")

    keys = r.keys("*")
    print(f"Number of keys: {len(keys)}")

    avg_key_size = sum(r.memory_usage(key) for key in keys) / len(keys)
    print(f"Avg key size: {avg_key_size:.2f} bytes")

    number_of_more_keys = memory_left // avg_key_size
    print(f"Number of more keys: {number_of_more_keys}")
