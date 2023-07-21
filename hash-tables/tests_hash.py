import pytest
from hash_tables import HashTable

@pytest.fixture
def hashtable():
    return HashTable()

def test_set_and_get(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    assert hashtable.get("key1") == "value1"
    assert hashtable.get("key2") == "value2"

def test_get_nonexistent_key(hashtable):
    assert hashtable.get("non_existent_key") is None

def test_get_keys(hashtable):
    hashtable.set("key1", "value1")
    hashtable.set("key2", "value2")
    hashtable.set("key3", "value3")
    assert set(hashtable.keys()) == {"key1", "key2", "key3"}

def test_collision_handling(hashtable):
    # Force a collision by using the same index after hashing
    # The collision will occur when the keys have the same hash
    # but are different keys
    hashtable.set("key1", "value1")
    hashtable.set("1key", "value2")
    assert hashtable.get("key1") == "value1"
    assert hashtable.get("1key") == "value2"

def test_hashing_in_range(hashtable):
    # Test if the hash value falls within the range [0, size-1]
    key = "test_key"
    size = 1024
    hash_value = hashtable._HashTable__hash(key)
    assert 0 <= hash_value < size
