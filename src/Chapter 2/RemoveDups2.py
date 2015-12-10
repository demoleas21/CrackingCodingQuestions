"""2.1 Remove Dupes"""

class Node(object):
    """Node Class"""
    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    @property
    def next(self):
        """Gets next node"""
        return self.next_node

    @next.setter
    def next(self):
        """Sets the next node"""
        self.next_node = n

    @property
    def data(self):
        """Gets value of node"""
        return self.data

    @data.setter
    def data(self):
        """Sets value of data"""
        self.data = d


class LinkedList(object):
    """Linked List Class"""
    def __init__(self, r=None):
        self.root = r

    def add(self, d):
        """Adds values to linked list"""
        new_node = Node(d, self.root)
        self.root = new_node

    def remove(self, d):
        """Removes values from linked list"""
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.data == d:
                if prev_node:
                    prev_node.next(this_node.next)
                else:
                    self.root = this_node
                return True
            else:
                prev_node = this_node
                this_node = this_node.next
        return False

    def display_list(self):
        """Displays Linked List elements"""
        this_node = self.root
        while this_node:
            print(this_node.data)
            this_node = this_node.next

    def find_dups(self):
        """Finds duplicate elements"""
        this_node = self.root
        dupe_table = {}
        while this_node:
            try:
                dupe_table[this_node.data] += 1
            except:
                dupe_table[this_node.data] = 1
            print(dupe_table)
            for key in dupe_table:
                if dupe_table[key] > 1:
                    mylist.remove(this_node.data)
            this_node = this_node.next
        print(dupe_table)



mylist = LinkedList()
mylist.add(8)
mylist.add(5)
mylist.add(12)
mylist.add(10)
print(mylist.remove(8))
print(mylist.remove(4))
mylist.display_list()
mylist.find_dups()
