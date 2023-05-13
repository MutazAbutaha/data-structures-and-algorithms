import pytest
from linked_list import Linked_List

def test_empty_list():
    new_list = Linked_List()
    actual = new_list.head
    expected = None
    assert actual == expected

def test_insert_node():
    new_list = Linked_List()
    new_list.insert("Inserted Node")
    actual = new_list.head.value
    expected = "Inserted Node"
    assert actual == expected

def test_first_head():     
    new_list = Linked_List()
    new_list.insert("First Node")
    actual = new_list.head.value
    expected = "First Node"
    assert actual == expected

def test_insert_nodes():
    new_list = Linked_List()
    new_list.insert(1)
    new_list.insert(2)
    actual1 = new_list.includes(1)
    actual2 = new_list.includes(2)
    expected = True
    assert actual1, actual2 == expected

def test_value_exists():
    new_list = Linked_List()
    new_list.insert(10)
    actual = new_list.includes(10)
    expected = True
    assert actual == expected

def test_value_not_exist():
    new_list = Linked_List()
    actual = new_list.includes(8)
    expected = False
    assert actual == expected

def test_list_values():
    new_list = Linked_List()
    new_list.insert('3')
    new_list.insert('2')
    new_list.insert('1')
    actual = new_list.to_string()
    expected = '{ 1 } -> { 2 } -> { 3 } -> NONE'
    assert actual == expected


@pytest.fixture(autouse=True)
def counter_reset():
    Linked_List.counter = 0