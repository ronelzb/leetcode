# https://leetcode.com/problems/sort-list/
# tags: #divide_and_conquer, #linked_list, #merge_sort, #sorting, #top_interview_questions, #two_pointers
#
# Solution: Merge sort
# 1. Divide and conquer, split the array in halves using hare-and-tortoise algorithm
# 2. Merge:
#   * To merge, we use the merge two linked lists from LC 21 (https://leetcode.com/problems/merge-two-sorted-lists/)
#   * We set a dummy node and a current node.
#   We then compare each node in left and right and set curr.next as the smaller of the two
#   * Eventually, one or both of them will be empty, curr.next is set as the remaining one or None
#   * Once the two sorted lists are merged, we return dummy.next
# Time complexity: O(n*log(n)), Space complexity O(log(n))
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-(sys.maxsize - 1))
        curr = dummy

        while l1 and l2:
            if l1.val > l2.val:
                curr.next, l2 = l2, l2.next
            else:
                curr.next, l1 = l1, l1.next
            curr = curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        return self.merge(self.sortList(head), self.sortList(slow))


if __name__ == "__main__":
    sol = Solution()
    h1 = ListNode(4)
    h1.next = ListNode(2)
    h1.next.next = ListNode(1)
    h1.next.next.next = ListNode(3)
    h1 = sol.sortList(h1)

    c = h1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
