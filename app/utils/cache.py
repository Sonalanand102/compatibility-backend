from time import time

CACHE = {}
CACHE_TTL = 60 * 60  # 1 hour


def _is_expired(entry):
    return time() - entry["timestamp"] > CACHE_TTL


def get_from_cache(key: str):
    entry = CACHE.get(key)

    if not entry:
        return None

    if _is_expired(entry):
        del CACHE[key]
        return None

    return entry["data"]


def set_to_cache(key: str, data):
    CACHE[key] = {
        "data": data,
        "timestamp": time()
    }
