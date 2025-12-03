import sys
import random
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from typing import *
from bst import *


sys.setrecursionlimit(10**6)


def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def sum_depths(node, depth=0):
    if node is None:
        return 0
    return depth + sum_depths(node.left, depth + 1) + sum_depths(node.right, depth + 1)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def average_depth(node):
    total_nodes = count_nodes(node)
    if total_nodes == 0:
        return 0
    return sum_depths(node) / total_nodes


def find_n_max_for_heights():
    heights = []
    n_values = []
    t = BST()
    for n in range(1, 2001):
        t.insert(random.randint(1, 1_000_000))
        h = height(t.root)
        n_values.append(n)
        heights.append(h)
        if h > 30:
            break
    return n_values, heights


def experiment_random_depths(trials=300):
    depths = []
    n_values = []
    for n in range(1, trials + 1):
        t = BST()
        for _ in range(n):
            t.insert(random.randint(1, 1_000_000))
        d = average_depth(t.root)
        depths.append(d)
        n_values.append(n)
    return n_values, depths


def experiment_sorted_depths(n_max=300):
    depths = []
    n_values = []
    t = BST()
    for n in range(1, n_max + 1):
        t.insert(n)
        d = average_depth(t.root)
        depths.append(d)
        n_values.append(n)
    return n_values, depths


if __name__ == "__main__":
    n_vals, heights = find_n_max_for_heights()
    plt.plot(n_vals, heights)
    plt.title("Tree Height vs N (Random Insertions)")
    plt.xlabel("N")
    plt.ylabel("Height")
    plt.show()

    n_vals, depths = experiment_random_depths()
    plt.plot(n_vals, depths)
    plt.title("Average Depth vs N (Random BSTs)")
    plt.xlabel("N")
    plt.ylabel("Average Depth")
    plt.show()

    n_vals, depths = experiment_sorted_depths()
    plt.plot(n_vals, depths)
    plt.title("Average Depth vs N (Sorted Insertions – Worst Case)")
    plt.xlabel("N")
    plt.ylabel("Average Depth")
    plt.show()
