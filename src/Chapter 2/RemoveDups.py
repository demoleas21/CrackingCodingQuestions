"""2.1 Remove Dupes"""

from unittest import TestCase

class Node(object):
    """Node Class"""
    def __init__(self):
        self.data = None
        self.next_node = None


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
        node_list = []
        while this_node:
            print(this_node.data)
            node_list.append(this_node.data)
            this_node = this_node.next_node
        print(node_list)

    def find_list(self):
        """Finds Linked List elements"""
        this_node = self.current_node
        node_list = []
        while this_node:
            node_list.append(this_node.data)
            this_node = this_node.next_node
        return node_list

    def del_dups(self):
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

class TestCases(TestCase):
    """Test Class"""
    def testRemoveOneDupe1(self):
        mylist.add(8)
        mylist.add(8)
        mylist.add(5)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 5, 8]
        assert mylist.find_list() == check_list

    def testRemoveOneDupe2(self):
        mylist.add(8)
        mylist.add(5)
        mylist.add(8)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 5, 8]
        print(mylist.find_list())
        assert mylist.find_list() == check_list

    def testRemoveOneDupe3(self):
        mylist.add(8)
        mylist.add(5)
        mylist.add(12)
        mylist.add(8)
        mylist.del_dups()
        check_list = [12, 5, 8]
        assert mylist.find_list() == check_list

    def testRemoveOneDupe4(self):
        mylist.add(5)
        mylist.add(8)
        mylist.add(8)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 8, 5]
        assert mylist.find_list() == check_list

    def testRemoveOneDupe5(self):
        mylist.add(5)
        mylist.add(8)
        mylist.add(12)
        mylist.add(8)
        mylist.del_dups()
        check_list = [12, 8, 5]
        assert mylist.find_list() == check_list

    def testRemoveOneDupe6(self):
        mylist.add(5)
        mylist.add(12)
        mylist.add(8)
        mylist.add(8)
        mylist.del_dups()
        check_list = [8, 12, 5]
        assert mylist.find_list() == check_list

    def testRemoveOneTrip1(self):
        mylist.add(8)
        mylist.add(8)
        mylist.add(8)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 8]
        assert mylist.find_list() == check_list

    def testRemoveOneTrip2(self):
        mylist.add(8)
        mylist.add(8)
        mylist.add(12)
        mylist.add(8)
        mylist.del_dups()
        check_list = [12, 8]
        assert mylist.find_list() == check_list

    def testRemoveOneTrip3(self):
        mylist.add(8)
        mylist.add(12)
        mylist.add(8)
        mylist.add(8)
        mylist.del_dups()
        check_list = [12, 8]
        assert mylist.find_list() == check_list

    def testRemoveOneTrip4(self):
        mylist.add(12)
        mylist.add(8)
        mylist.add(8)
        mylist.add(8)
        mylist.del_dups()
        check_list = [8, 12]
        assert mylist.find_list() == check_list

    def testRemoveTwoDupes1(self):
        mylist.add(8)
        mylist.add(8)
        mylist.add(12)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 8]
        assert mylist.find_list() == check_list

    def testRemoveTwoDupes2(self):
        mylist.add(8)
        mylist.add(12)
        mylist.add(8)
        mylist.add(12)
        mylist.del_dups()
        check_list = [12, 8]
        assert mylist.find_list() == check_list

    def testRemoveTwoDupes3(self):
        mylist.add(8)
        mylist.add(12)
        mylist.add(12)
        mylist.add(8)
        mylist.del_dups()
        check_list = [8, 12]
        assert mylist.find_list() == check_list

    def testRemoveNoDupes(self):
        mylist.add(8)
        mylist.add(5)
        mylist.add(12)
        mylist.add(9)
        mylist.del_dups()
        check_list = [9, 12, 5, 8]
        assert mylist.find_list() == check_list
