import re
class Node :
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Linked_List:
   
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def to_string(self):
        current = self.head
        values = ""
        while current:
            values += f"{ {current.value} } -> "
            list_values = re.sub(r"\'", ' ', values)
            current = current.next
        list_values += "NONE"
        return list_values
    
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        if self.head.value == value:
            # If the value is found at the head, insert the new node before it
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                # If the value is found in the next node, insert the new node before it
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        # If the value is not found in the list, the new node will be added at the end
        current.next = new_node

    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        current = self.head
        while current:
            if current.value == value:
                # If the value is found, insert the new node after it
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    def kthFromEnd(self, k):
        if self.head is None:
            return "Linked list is empty."
        first = self.head
        second = self.head
        count = 0
        while count < k:
            if second.next is None:
                return "Exception"
            second = second.next
            count += 1
# moves the second pointer k steps from ahead
# count to  track of the number of steps
        while second.next:
            first = first.next
            second = second.next
# move the first and second pointers
# second reaches the last node
# first pointer ends up at the node that is k steps
        return first.value

    def traverse(self):
        current = self.head
        while current:
            print(f'{{{current.value}}} ->', end=' ')
            current = current.next
        print('X')