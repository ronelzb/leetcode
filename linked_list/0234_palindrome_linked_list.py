# https://leetcode.com/problems/palindrome-linked-list/
# tags: #recursion, #stack, #two_pointers, #top_interview_questions
#
# Solution 1: Stack
# Find the middle node using a slow and fast pointer traversal to the linked list
# From the middle to the end append each node values to the stack
# Check each node from head until the stack is empty
# Time complexity: O(n), Space complexity O(n)
#
# Solution Follow-up: Two Pointers
# In order to achieve a solution in O(n) and no additional space we need to do the following:
# * Find previous to middle node using a slow and fast pointer traversal to the linked list
# * Get the middle (next) node and unlink the list on the previous to middle node.
# * From middle, reverse the second half and at the end get the first reversed node (last one previously)
# * Traverse first and second half checking both values at each position
# Time complexity: O(n), Space complexity O(1)
from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def isPalindrome_stack(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = deque()
        while slow:
            stack.append(slow.val)
            slow = slow.next

        slow = head
        while stack:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True

    def isPalindrome_followup(self, head: Optional[ListNode]) -> bool:
        if head.next is None: return True

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        current = prev
        slow = head
        while current and slow:
            if current.val != slow.val:
                return False
            current = current.next
            slow = slow.next

        return True


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    print(sol.isPalindrome_stack(l1))  # True
