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

def test_append_to_end():
    my_list = Linked_List()
    my_list.append(2)
    assert my_list.head.value == 2
    assert my_list.head.next is None
    my_list.append(5)
    assert my_list.head.next.value == 5
    assert my_list.head.next.next is None
def test_append_multiple_nodes():
    my_list = Linked_List()
    my_list.append(2)
    my_list.append(5)
    my_list.append(8)
    assert my_list.head.value == 2
    assert my_list.head.next.value == 5
    assert my_list.head.next.next.value == 8
    assert my_list.head.next.next.next is None
def test_insert_before_middle_node():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(3)
    my_list.append(4)
    my_list.insert_before(3, 2)
    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next.value == 4
    assert my_list.head.next.next.next.next is None
def test_insert_before_first_node():
    my_list = Linked_List()
    my_list.append(2)
    my_list.append(3)
    my_list.insert_before(2, 1)
    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next is None
def test_insert_after_middle_node():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(2)
    my_list.append(4)
    my_list.insert_after(2, 3)
    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next.value == 4
    assert my_list.head.next.next.next.next is None
def test_insert_after_last_node():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(2)
    my_list.insert_after(2, 3)
    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next is None

def test_kthFromEnd_greater_than_length():
    my_list = Linked_List()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    assert my_list.kthFromEnd(4) == "Exception"
def test_kthFromEnd_length_and_k_are_same():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    assert my_list.kthFromEnd(3) == "Exception"
def test_kthFromEnd_negative_k():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    assert my_list.kthFromEnd(-2) == 3
def test_kthFromEnd_size_1_list():
    single_node_list = Linked_List()
    single_node_list.append(1)
    assert single_node_list.kthFromEnd(0) == 1
def test_kthFromEnd_middle_node():
    my_list = Linked_List()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    assert my_list.kthFromEnd(2) == 2

@pytest.fixture(autouse=True)
def counter_reset():
    Linked_List.counter = 0