# https://leetcode.com/problems/linked-list-cycle/
# tags: #blind_75_must_do, #hash_table, #linked_list, #two_pointers, #top_interview_questions
#
# Solution: Two pointers
# Classical tortoise and hare algorithm to try to identify if there is a cycle when slow == fast
# after traversing the linked list with a slow and fast pointers
# Time complexity: O(n), Space complexity: O(1)
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow, fast = head, head.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        return fast and slow == fast


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(3)
    h.next = ListNode(2)
    h.next.next = ListNode(0)
    h.next.next.next = ListNode(-4)
    h.next.next.next.next = h.next

    print(sol.hasCycle(head=h))  # True

    h = ListNode(1)
    print(sol.hasCycle(head=h))  # False
