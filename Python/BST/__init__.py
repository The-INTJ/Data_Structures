# Implementation of a binary search tree


class Node:

    def __init__(self, val):
        self.data = val  # Saving the passed value
        self.left_node = None
        self.right_node = None

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left_node

    def get_right(self):
        return self.right_node

    def set_right(self, new_right):
        self.right_node = new_right

    def set_left(self, new_left):
        self.left_node = new_left


class BinarySearchTree:

    def __init__(self):  # __init__(self, root = None)
        self.root = None

    def get_root(self):
        return self.root

    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.get_left())
            print(root.get_data())
            self._inorder(root.get_right())

    def insert(self, data):
            if self.root is None:
                self.root = Node(data)
            else:
                self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.get_data():
            if root.get_left() is not None:
                self._insert(root.get_left(), data)
            else:
                root.set_left(Node(data))
        else:
            if root.get_right() is not None:
                self._insert(root.get_right(), data)
            else:
                root.set_right(Node(data))

    def levels(self):
        if self.root is None:
            print(0)
        else:
            print(self._levels(self.root))

    def _levels(self, root):
        if root is not None:
            return 1 + max(self._levels(root.get_left()), self._levels(root.get_right()))
        else:
            return 0


bst = BinarySearchTree()
bst.insert(3)
bst.insert(2)
bst.insert(9)
bst.insert(4)
bst.insert(1)
bst.insert(5)
bst.insert(7)
bst.insert(6)

bst.inorder()
print()
bst.levels()  # Height
