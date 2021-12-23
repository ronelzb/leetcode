# https://leetcode.com/problems/linked-list-cycle-ii/
# tags: #two_pointers
#
# Solution: Two Pointers
# Classical tortoise and the hare solution taking a slow and fast pointer respectively.
# In the first find if there is actually a cycle where slow == fast
# If this happens then find the cycle start repointing fast from head
# Graphical explanation at:
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
# Time complexity: O(n), Space complexity O(1)
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: break

        if slow != fast: return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


if __name__ == "__main__":
    sol = Solution()

    h1 = ListNode(3)
    h1.next = ListNode(2)
    h1.next.next = ListNode(0)
    h1.next.next.next = ListNode(-4)
    h1.next.next.next.next = h1.next
    print(sol.detectCycle(h1))  # 2

    h1 = ListNode(1)
    h1.next = ListNode(2)
    h1.next.next = h1
    print(sol.detectCycle(h1))  # 1

    h1 = ListNode(1)
    print(sol.detectCycle(h1))  # None
