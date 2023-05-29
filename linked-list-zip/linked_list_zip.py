class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def to_string(self):
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def zip_lists(self, list_one, list_two):
        if list_one.head is None:
            return list_two
        if list_two.head is None:
            return list_one
        curr_one = list_one.head
        curr_two = list_two.head
        while curr_one is not None and curr_two is not None:
            next1 = curr_one.next
            next2 = curr_two.next
            curr_one.next = curr_two
            curr_two.next = next1 or next2
            curr_one = next1
            curr_two = next2
        return list_one.to_string()
    
linked_list_one = LinkedList()
linked_list_one.append(1)
linked_list_one.append(2)
linked_list_one.append(3)
linked_list_two = LinkedList()
linked_list_two.append(4)
linked_list_two.append(5)
linked_list_two.append(6)
zip = linked_list_one.zip_lists(linked_list_one, linked_list_two)
print(zip)


