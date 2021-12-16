# https://leetcode.com/problems/insertion-sort-list/
# tags: #linked_list, #sorting
#
# Solution: Sort by swapping nodes
# Using insertion sort we need to remove current from its original position and insert it at its correct position:
# * Update current.next to behind which is the position before which current needs to be inserted.
# * Update next pointer of previous behind node (behind_prev.next) because current is now inserted before behind.
# * Update next pointer of previous current node (curr_prev.next) because current was removed previously from here.
# Time complexity: O(n^2), Space complexity O(1)
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-(sys.maxsize - 1), head)
        curr_prev, current = head, head.next

        while current:
            curr_next = current.next

            if current.val > curr_prev.val:
                curr_prev = current
            else:
                behind_prev, behind = dummy, dummy.next

                while behind.val < current.val:
                    behind_prev, behind = behind, behind.next

                current.next = behind
                behind_prev.next = current
                curr_prev.next = curr_next

            current = curr_next

        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    h1 = ListNode(4)
    h1.next = ListNode(2)
    h1.next.next = ListNode(1)
    h1.next.next.next = ListNode(3)
    h1 = sol.insertionSortList(h1)

    c = h1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
