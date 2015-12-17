"""3.1 Three In One"""

class Stack(object):
    """Stack Data Structure"""
    def __init__(self):
        self.container = []

    def push(self, data):
        """Adds data to stack"""
        self.container.append(data)

    def pop(self):
        """Removes the top element"""
        self.container.pop()

    def peek(self):
        """Display the top of stack"""
        return self.container[len(self.container)-1]

    def size(self):
        """Display size of stack"""
        return len(self.container)

    def is_empty(self):
        """Informs if stack is empty"""
        return self.container == []


class Queue(object):
    """Queue Data Structure"""
    def __init__(self):
        self.container = []

    def push(self, data):
        """Adds data to queue"""
        self.container.append(data)

    def pop(self):
        """Removes the top element"""
        self.container.pop(0)

    def peek(self):
        """Display the top of queue"""
        return self.container[0]

    def size(self):
        """Display size of queue"""
        return len(self.container)

    def is_empty(self):
        """Informs if stack is empty"""
        return self.container == []


stack=Stack()
stack.push(1)
stack.push(2)
print(stack.size())
stack.pop()
print(stack.peek())
print(stack.is_empty())
stack.pop()
print(stack.is_empty())

queue=Queue()
queue.push(1)
queue.push(2)
print(queue.size())
queue.pop()
print(queue.peek())
print(queue.is_empty())
queue.pop()
print(queue.is_empty())
