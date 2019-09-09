# Thanks and credit to John Shiver on Code Fellows (https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/)
# I followed his guide to create this, and then worked to add a few of my own methods



# The Node class. Each item in the linked list will be composed of one of these
#lowercase 'class' declare
class Node(object):

    #This is python's constructor. Every class needs to define this, it is what
    # will be called when the class is invoked
    # --
    # Also notice that the declarations for the variables are IN the constructor
    def __init__(self, data=None, next_node=None):
        self.data = data # Saving the passed value
        self.next_node = next_node # A complicated part


    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        size = 0
        tracker_node = self.head
        while tracker_node is not None: # Spelled out, but unnecessary
            size = size + 1
            tracker_node = tracker_node.next_node
        return size

    def search(self, data):
        current = self.head
        found = False
        while current is not None and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current














