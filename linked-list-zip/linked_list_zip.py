class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


def zipLists(list1, list2):
    if not list1:  # If list1 is empty, return list2
        return list2
    if not list2:  # If list2 is empty, return list1
        return list1
    # Create a dummy node to serve as the head of the new list
    dummy = Node(0)
    current = dummy  # Pointer to the current node in the new list
    while list1 and list2:
        # Add the current node from list1 to the new list
        current.next = list1
        list1 = list1.next
        current = current.next
        # Add the current node from list2 to the new list
        current.next = list2
        list2 = list2.next
        current = current.next
    # If list1 is longer than list2, add the remaining nodes
    if list1:
        current.next = list1
    # If list2 is longer than list1, add the remaining nodes
    if list2:
        current.next = list2
    return dummy.next  # Return the head of the new list

