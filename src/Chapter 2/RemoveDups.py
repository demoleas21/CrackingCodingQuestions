"""2.1 Remove Dupes"""

class Node(object):
    """Node Class"""
    def __init__(self):
        self.data = None
        self.next_node = None
"""
    @property
    def next_node(self):
        Gets next node
        return self._next_node

    @next_node.setter
    def next_node(self, n):
        Sets the next node
        self.next_node = n

    @property
    def data(self):
        Gets value of node
        return self._data

    @data.setter
    def data(self, d):
        Sets value of data
        self.data = d
"""

class LinkedList(object):
    """Linked List Class"""
    def __init__(self):
        self.current_node = None

    def add(self, d):
        """Adds values to linked list"""
        new_node = Node()
        new_node.data = d
        new_node.next_node = self.current_node
        self.current_node = new_node

    def remove(self, d):
        """Removes values from linked list"""
        this_node = self.current_node
        prev_node = None
        while this_node:
            if this_node.data == d:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                    return True
                else:
                    self.current_node = this_node.next_node
                    return True
            prev_node = this_node
            this_node = this_node.next_node
        return False

    def display_list(self):
        """Displays Linked List elements"""
        this_node = self.current_node
        while this_node:
            print(this_node.data)
            this_node = this_node.next_node

    def find_dups(self):
        """Finds duplicate elements"""
        this_node = self.current_node
        dupe_table = {}
        while this_node:
            table_check = dupe_table.get(this_node.data, 0)
            dupe_table[this_node.data] = table_check + 1
            for key in dupe_table:
                if dupe_table[key] > 1:
                    mylist.remove(this_node.data)
            this_node = this_node.next_node



mylist = LinkedList()
mylist.add(8)
mylist.add(5)
mylist.add(12)
mylist.add(8)
print(mylist.remove(12))
print(mylist.remove(4))
mylist.display_list()
mylist.find_dups()
mylist.display_list()
