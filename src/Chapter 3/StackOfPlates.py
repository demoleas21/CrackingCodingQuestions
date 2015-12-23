"""3.3 Stack of Plates"""

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


class StackSet(Stack):
    """Set of stacks"""

    def push(self, data):
        """Adds data to set of stacks"""
        pass    

    def pop(self):
        """Removes the top element of the set"""
        pass

    def peek(self):
        """Display the top of the set"""
        pass

    def size(self):
        """Display size of set"""
        pass

    def is_empty(self):
        """Informs if the set is empty"""
        pass


