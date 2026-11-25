import valkey
from loguru import logger

# Connect to Valkey cache server
cache_client = valkey.Valkey()
logger.info("Connected to Valkey server: {}", cache_client.ping())

# Put data into cache
def put(key, value):
    resp = cache_client.set(key, value)
    if not resp:
        logger.error(f"Failed to set key {key} in cache.")

# Retrieve data from cache
def get(key):
    resp = cache_client.get(key)
    if resp is None:
        logger.warning(f"Key {key} not found in cache.")
    return resp