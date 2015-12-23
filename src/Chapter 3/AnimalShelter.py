"""3.6 Animal Shelter"""

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
