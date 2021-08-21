# https://leetcode.com/problems/add-two-numbers-ii/
# tags: #linked_list, #math, #numbers, #recursion
# Idea:
# 1. Since input lists have different sizes it is a good idea to get the sizes of each to determine which one
# is longest/shortest and a delta to know when to take shortest into the sum.
# 2. When iterating in both lists we will get the sum and store into a new reversed list as it is
# (10 or greater can be a value in this staging list)
# 3. The idea to store the values in a reversed list is when we reverse it back to get the final result
# we can determine the carry at each one, from the least significant number
# Time complexity: O(2 * max(l1, l2)) => O(max(l1, l2)), Space complexity: O(max(l1, l2)) + 1 if carry at the end
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m, n = self.get_list_size(l1), self.get_list_size(l2)
        delta = abs(m - n)
        longest_list = l1 if m >= n else l2
        shortest_list = l2 if longest_list == l1 else l1
        head = None

        i = 0
        while longest_list:
            value = longest_list.val
            longest_list = longest_list.next

            if i >= delta:
                value += shortest_list.val
                shortest_list = shortest_list.next

            new_node = ListNode(value)
            new_node.next = head
            head = new_node
            i += 1

        return self.reverse_list(head)

    def get_list_size(self, head: ListNode):
        size = 0
        while head:
            size += 1
            head = head.next
        return size

    def reverse_list(self, head: ListNode):
        prev = None
        carry = 0

        while head:
            head.val += carry
            if head.val >= 10:
                head.val %= 10
                carry = 1
            else:
                carry = 0

            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        if carry > 0:
            new_node = ListNode(1)
            new_node.next = prev
            prev = new_node

        return prev


if __name__ == "__main__":
    sol = Solution()

    list1 = ListNode(7)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list1.next.next.next = ListNode(3)

    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)

    c = result = sol.addTwoNumbers(list1, list2)  # 7 -> 8 -> 0 -> 7
    while c:
        print(c, end=" -> ")
        c = c.next
