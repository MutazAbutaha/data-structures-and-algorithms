class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception("PseudoQueue is empty")

        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

        return self.stack2.pop()


# Example usage
queue = PseudoQueue()
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(5)

print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 15
print(queue.dequeue())  # Output: 20
print(queue.dequeue())  # Output: 5
