# https://leetcode.com/problems/merge-two-sorted-lists/
# tags: #linked_list, #must_do_easy_questions, #recursion, #top_interview_questions
#
# Solution: One pass iteration
# Fill up a new list while list1 or list 2 have nodes, at each iteration compare if one of those 2 has nodes
# If both have nodes available then compare which nodes' values is the smallest
# Time complexity: O(m+n), Space complexity: O(m+n)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3, current = None, None

        while list1 or list2:
            if current:
                current.next = ListNode()
                current = current.next
            else:
                current = ListNode()
                list3 = current

            if list1 and (not list2 or list1.val <= list2.val):
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

        return list3


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    sol = Solution()
    l3 = sol.mergeTwoLists(l1, l2)

    while l3:
        print(l3.val)
        l3 = l3.next
