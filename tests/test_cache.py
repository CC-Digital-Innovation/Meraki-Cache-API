import src.cache as cache

# TODO: Find a way to mock the Valkey client for testing purposes, so we don't rely on an actual Valkey server during tests.

def test_put_cache():
    key = "test_key"
    value = "test_value"
    
    cache.put(key, value)
    cached_value = cache.get(key)
    
    assert cached_value is not None
    assert cached_value == value
    
def test_get_cache_miss():
    key = "non_existent_key"
    
    cached_value = cache.get(key)
    
    assert cached_value is None