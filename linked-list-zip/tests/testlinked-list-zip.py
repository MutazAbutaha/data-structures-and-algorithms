import pytest
from linked_list_zip import zipLists , insert

def test_insert_nodes():
    new_list1 = insert()
    new_list1.insert(1)
    new_list1.insert(2)

    new_list2 = insert()
    new_list2.insert(3)
    new_list2.insert(4)
    new_list2.insert(5)




def test_zipLists(new_list1, new_list2, expected):
    assert zipLists(new_list1, new_list2) == expected



