"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:  # edge case: no node
            return None

        old_to_new = {}  # hashmap

        def dfs(node):  # depth-first search
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)  # create new node copy
            old_to_new[node] = copy  # add new node copy to the hashmap

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))  # recursively copy all other neighbors

            return copy

        return dfs(node)
