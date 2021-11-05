# https://leetcode.com/problems/partition-list/
# tags: #linked_list, #two_pointers
#
# Solution: Two pointers
# Let's set two pointers: One to store values that are less than x and current pointer to traverse the list
# First check if the visited value is greater or equal to x we simply move the current pointer
# But there is a catch: For the edge case we can have the very first set of values less than x
# In this case move prev pointer along with current
# When the value is less than x and prev counter is behind current then we need to arrange
# prev.next = current.next and re point all sub sequent values for prev and current accordingly
# Time complexity: O(n), Space complexity O(1)
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = current = head = dummy

        while current and current.next:
            if current.next.val >= x or prev == current:
                if current.next.val < x and prev == current: prev = prev.next
                current = current.next
            else:
                next_to_curr = current.next
                current.next = current.next.next
                next_to_prev = prev.next
                prev.next = next_to_curr
                next_to_curr.next = next_to_prev
                prev = next_to_curr

        return head.next


if __name__ == "__main__":
    sol = Solution()

    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(0)
    l1.next.next.next.next = ListNode(2)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(2)
    l1 = sol.partition(head=l1, x=3)  # [1,0,2,2,4,3,5]

    c = l1
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
