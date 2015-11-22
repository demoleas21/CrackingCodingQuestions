""" 2.1 Remove Dups """

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
    def display_list (self):
        this_node = self.root
        while this_node:
            print (this_node.get_data())
            this_node = this_node.get_next()
    def find_dups (self):
        this_node = self.root
        dupe_table = {}
        while this_node:
            try:
                dupe_table[this_node.get_data()] += 1
            except:
                dupe_table[this_node.get_data()] = 1
            print(dupe_table)
            for key in dupe_table:
                if dupe_table[key] > 1:
                    MyList.remove(this_node.get_data())
            this_node = this_node.get_next()
        print (dupe_table)



MyList = LinkedList()
MyList.add(8)
MyList.add(5)
MyList.add(12)
MyList.add(8)
print(MyList.remove(8))
print(MyList.remove(4))
MyList.display_list()
MyList.find_dups()
