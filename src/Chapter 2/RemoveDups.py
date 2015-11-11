""" 2.1 Remove Dups """

<<<<<<< HEAD
class Node(object):
    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n
    def get_next (self):
        return self.next_node
    def set_next (self):
        self.next_node = n
    def get_data (self):
        return self.data
    def set_data (self):
        self.data = d
||||||| merged common ancestors
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
=======
class OccupiedNodeError(Exception):
    """ The next node is occupied and cannot be added """

class LinkedList:
    """ Allows for Nodes to not worry about the head value and allows all
     external references to simply point to the head property of the linked
     list """
    def __init__(self, head=None):
        self.head = head
>>>>>>> e70b7f6ca7e7af25539b9b6c6ec6062735722c9d

<<<<<<< HEAD
class LinkedList (object):
    def __init__ (self, r = None):
        self.root = r
        self.size = 0
    def get_size (self):
        return self.size
    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
    def remove (self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
||||||| merged common ancestors
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current
=======

class Node:
    """ Singly Linked List Node """
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    def addNode(self, data):
        if type(data) != type(self):
            nextNode = Node(data)
        else:
            nextNode = data
>>>>>>> e70b7f6ca7e7af25539b9b6c6ec6062735722c9d

<<<<<<< HEAD
MyList = LinkedList()
MyList.add(5)
MyList.add(8)
MyList.add(12)
print(MyList.remove(12))
print(MyList.remove(4))
print(MyList.remove(12))
||||||| merged common ancestors
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
=======
        if not self.next:
            self.next = nextNode
        else:
            raise OccupiedNodeError(
                'The data value {0} cannot be added because the next node'\
                'already exists'.format(data))
>>>>>>> e70b7f6ca7e7af25539b9b6c6ec6062735722c9d
