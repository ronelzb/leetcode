# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# tags: #linked_list, #two_pointers
#
# Solution: Two Pointers
# Intuition: According to the problem statement we need to swap k - 1 and n - k nodes
# Find the size of the linked list first (n)
# Then, iterate the list to find both nodes and eventually swap them
# Time complexity: O(n), Space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        i = 0
        current = head
        start = end = None
        while i <= k - 1 or i <= n - k:
            if i == k - 1: start = current
            if i == n - k: end = current
            current = current.next
            i += 1

        start.val, end.val = end.val, start.val

        return head


if __name__ == "__main__":
    sol = Solution()

    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = ListNode(3)
    h1.next.next.next = ListNode(4)
    h1.next.next.next.next = ListNode(5)

    c = h1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")

    h1 = sol.swapNodes(head=h1, k=2)  # [1,4,3,2,5]

    c = h1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
