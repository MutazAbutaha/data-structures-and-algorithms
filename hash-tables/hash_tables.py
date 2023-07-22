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
