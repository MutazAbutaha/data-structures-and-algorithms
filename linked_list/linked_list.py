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
    