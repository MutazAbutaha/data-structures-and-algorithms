import pytest
from hashmap_repeated_word import HashTable

def test_repeated_word():
    # Create an instance of the class
    hash_table = HashTable()

    # Test case 1: No repeated word
    input_string1 = "This is a test string. Is this test working?"
    words1 = input_string1.lower().split()
    for word in words1:
        hash_table.set(word, 1)
    assert hash_table.find_first_repeated_word() is None

    # Test case 2: First repeated word is "this"
    input_string2 = "This is a test string. Is this test working? this"
    words2 = input_string2.lower().split()
    for word in words2:
        hash_table.set(word, 1)
    assert hash_table.find_first_repeated_word() == "this"

    # Test case 3: First repeated word is "is"
    input_string3 = "This is a test string. Is this test working? is this"
    words3 = input_string3.lower().split()
    for word in words3:
        hash_table.set(word, 1)
    assert hash_table.find_first_repeated_word() == "is"

    # Test case 4: No repeated word in an empty hash table
    assert hash_table.find_first_repeated_word() is None

    # Test case 5: No repeated word with only one word
    hash_table.set("hello", 1)
    assert hash_table.find_first_repeated_word() is None

    # Test case 6: First repeated word with the same word multiple times
    input_string4 = "apple apple orange orange banana banana"
    words4 = input_string4.lower().split()
    for word in words4:
        hash_table.set(word, 1)
    assert hash_table.find_first_repeated_word() == "apple"

if __name__ == "__main__":
    pytest.main()
