# https://leetcode.com/problems/copy-list-with-random-pointer/
# tags: #hash_table, #linked_list
#
# Solution: Copy linked list using a dictionary
# The solution traverses the linked list twice:
# 1. Store all nodes in the dictionary.
# 2. In the second pass, set next and random pointers to the values stored in the dictionary
# Time complexity: O(n), Space complexity O(n)
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        pointers = {}
        current = head
        while current:
            pointers[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            if current.next: pointers[current].next = pointers[current.next]
            if current.random: pointers[current].random = pointers[current.random]
            current = current.next

        return pointers[head]
