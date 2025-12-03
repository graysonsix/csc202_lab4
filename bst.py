import sys
import unittest
from typing import *
from dataclasses import dataclass


sys.setrecursionlimit(10 ** 6)


BinTree = Union[None, "Node"]


@dataclass(frozen=True)
class Node:
    value: Any
    left: BinTree
    right: BinTree


# Binary search tree class (mutable root)
class BST:
    def __init__(self, comes_before=lambda a, b: a < b):
        self.function = comes_before
        self.root = None

    # Returns true if BST is empty

    def is_empty(self):
        return self.root is None

    # Inserts a new value into the BST

    def insert(self, value):
        def helper(tree, value):
            if tree is None:
                return Node(value, None, None)
            if self.function(value, tree.value):
                return Node(tree.value, helper(tree.left, value), tree.right)
            else:
                return Node(tree.value, tree.left, helper(tree.right, value))

        self.root = helper(self.root, value)

    # Returns true if value is in the bst

    def lookup(self, value):
        def helper(tree, value):
            if tree is None:
                return False
            if not self.function(value, tree.value) and not self.function(tree.value, value):
                return True
            if self.function(value, tree.value):
                return helper(tree.left, value)
            else:
                return helper(tree.right, value)

        return helper(self.root, value)
