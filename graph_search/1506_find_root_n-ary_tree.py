# https://leetcode.com/problems/power-of-four/
# tags: #bit_manipulation, #dfs, #google, #hash_table, #tree
#
# Solution: Set
# For each element in the input list, put its child nodes in a set, since the value of each node is unique.
# We visit the list again, checking which node does not exist in the set.
# Time complexity: O(n), Space complexity: O(n)

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        seen = set()

        for node in tree:
            for child in node.children:
                seen.add(child.val)

        for node in tree:
            if node.val not in seen:
                return node
