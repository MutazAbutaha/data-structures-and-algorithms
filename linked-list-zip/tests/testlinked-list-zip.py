import pytest
from linked_list_zip import LinkedList

def test_zip_lists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2 = LinkedList()
    list2.append(4)
    list2.append(5)
    list2.append(6)
    actual = list1.zip_lists(list1, list2)
    expected = "{ 1 } -> { 4 } -> { 2 } -> { 5 } -> { 3 } -> { 6 } -> NONE"
    assert actual == expected

def test_zip_lists_one_longer():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    list2 = LinkedList()
    list2.append(6)
    list2.append(7)
    actual = list1.zip_lists(list1, list2)
    expected = "{ 1 } -> { 6 } -> { 3 } -> { 7 } -> { 2 } -> NONE"
    assert actual == expected

def test_zip_lists_two_longer():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list2 = LinkedList()
    list2.append(5)
    list2.append(6)
    list2.append(4)
    actual = list1.zip_lists(list1, list2)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 6 } -> { 4 } -> NONE"
    assert actual == expected
