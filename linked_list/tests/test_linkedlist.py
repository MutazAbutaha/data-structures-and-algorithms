import pytest
from linked_list.linked_list import   Linked_List
def test_empty_linked_list():
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
def test_first_node_is_head():      # !!!!
    new_list = Linked_List()
    new_list.insert("First Node")
    actual = new_list.head.value
    expected = "First Node"
# def test_insert_multiple_nodes():
#     new_list = Linked_List()
#     new_list.insert(1)
#     new_list.insert(2)
#     nodes_num = 2
#     actual = Linked_List.counter
#     expected = nodes_num
#     assert actual == expected
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
def test_linked_list_values():
    new_list = Linked_List()
    new_list.insert('C')
    new_list.insert('B')
    new_list.insert('A')
    actual = new_list.to_string()
    expected = '{ A } -> { B } -> { C } -> NONE'
    assert actual == expected
@pytest.fixture(autouse=True)
def counter_reset():
    Linked_List.counter = 0