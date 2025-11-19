import sys
import unittest
from typing import *
from dataclasses import dataclass

sys.setrecursionlimit(10 ** 6)

BinTree: TypeAlias = Union[None, 'Node']


@dataclass(frozen=True)
class Node:
    Value: any
    left: BinTree
    right: BinTree


@dataclass(frozen=True)
class BinarySearchTree:
    function: Callable[[Any, Any], bool]
    root: BinTree


# Returns true if A comes before B
def comes_before(a: any, b: any) -> bool:
    return a < b


# Returns true if BST is empty
def is_empty(bst: BinarySearchTree) -> bool:
    if bst.root is None:
        return True
    else:
        return False


# Inserts a new value into the BST
def insert(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if tree is None:
            return Node(value, None, None)
        if comes_before(value, tree.value):
            return Node(tree.value, helper(tree.left, value), tree.right)
        else:
            return Node(tree.value, tree.left, helper(tree.right, value))
        root = helper(bst, value, bst.function)
        return BinarySearchTree(bst.function, new_root)


# Returns true if value is in the bst
def lookup(bst: BinarySearchTree, value: Any) -> bool:
    def helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> bool:
        if tree is None:
            return False
        if not comes_before(value, tree.value) and not comes_before(tree.value, value):
            return True
        if comes_before(tree.value, value):
            return helper(tree.left, value, comes_before)
        else:
            return helper(tree.right, value, comes_before)

    return helper(bst.root, value, bst.function)


#
def delete(bst: BinarySearchTree, value: Any) -> BinarySearchTree:
    def helper(tree: BinTree, value: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        if tree is None:
            return None
        if not comes_before(value, tree.Value) and not comes_before(tree.Value, value):
            if tree.left is None and tree.right is None:
                return None
            elif tree.left is None:
                return tree.right
            elif tree.right is None:
                return tree.left
            else:
                next_value = find_min_value(tree.right)
                new_right = helper(tree.right, next_value, comes_before)
                return Node(next_value, tree.left, new_right)
        elif comes_before(value, tree.value):
            return Node(tree.Value, helper(tree.left, value, comes_before), tree.right)
        else:
            return Node(tree.Value, tree.left, helper(tree.right, value, comes_before))


def find_min_value(bst: BinarySearchTree) -> Any:
    if bst is None:
        return bst.value
    else:
        return find_min_value(bst.left)