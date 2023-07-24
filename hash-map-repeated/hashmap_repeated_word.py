from functools import reduce
from operator import add

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.__keys = []  # Renamed the attribute to avoid conflicts

    def __hash(self, key):
        return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert(self, value):
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

        def find_first_repeated_value(self):
            # Helper method to find the first value that occurs more than once in the linked list
            freq_map = {}
            current = self.head
            while current:
                # Convert the list to a tuple before using it as a key
                current_value_tuple = tuple(current.value)
                if current_value_tuple in freq_map:
                    return current.value
                freq_map[current_value_tuple] = 1
                current = current.next
            return None

    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = self.LinkedList()  # Create a LinkedList instance
            self.__buckets[index] = ll

        self.__buckets[index].insert([key, value])
        self.__keys.append(key)

    def get(self, key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None

    def has(self, key):
        return self.get(key) is not None

    def keys(self):
        return self.__keys

    def find_first_repeated_word(self):
        # Main method that finds the first word to occur more than once in the hash table
        for bucket in self.__buckets:
            if bucket is not None:
                first_repeated_value = bucket.find_first_repeated_value()
                if first_repeated_value:
                    return first_repeated_value[0]
        return None

hash_table = HashTable()

# Set key-value pairs
hash_table.set("apple", 5)
hash_table.set("banana", 2)
hash_table.set("orange", 3)
hash_table.set("apple", 10)

# Find the first repeated word
repeated_word = hash_table.find_first_repeated_word()
print(repeated_word)  # Output: "apple"