import valkey
from loguru import logger

from meraki_data_collector import get_org_networks

# Connect to the cache.
CACHE_CLIENT = valkey.Valkey()

# Put data into cache
def put(key, value):
    resp = CACHE_CLIENT.set(key, value)
    if not resp:
        logger.error(f"Failed to set key {key} in cache.")

# Retrieve data from cache
def get(key):
    resp = CACHE_CLIENT.get(key)
    if resp is None:
        logger.warning(f"Key {key} not found in cache.")
    return resp

def main():
    # TODO: Enable JSON module in Valkey to allow for storing and retrieving JSON data.
    org_networks = get_org_networks()
    if not org_networks:
        logger.error("Failed to fetch organization networks.")
        return
    CACHE_CLIENT.set(name="org_networks", value=org_networks)
    networks_from_cache = CACHE_CLIENT.get(name="org_networks")
    print(networks_from_cache)
    

if __name__ == "__main__":
    main()
