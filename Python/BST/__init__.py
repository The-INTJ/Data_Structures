# Implementation of a binary search tree

class Node:

    def __init__(self, data=None, left_node=None, right_node=None):
        self.data = data  # Saving the passed value
        self.left_node = left_node  # Points to itself
        self.right_node = right_node

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

    def __init__(self, left=None, right=None):
        self.left = left