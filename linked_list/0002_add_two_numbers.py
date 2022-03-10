# https://leetcode.com/problems/add-two-numbers/
# tags: #google, #linked_list, #math, #numbers, #recursion
#
# Solution: List traversal
# The idea is to traverse both lists summing the digits at each position
# We already have those lists in reversed order, so we can go and traverse them directly using a carry
# to keep it consistent when a sum exceeds 9
# Dummy node at the beginning is useful to avoid extra validations
# Time complexity: O(max(l1, l2)), Space complexity: O(max(l1, l2))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(0)
        carry = 0

        while l1 or l2:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            current = current.next
            carry //= 10

        if carry > 0:
            current.next = ListNode(carry)

        return head.next


if __name__ == "__main__":
    sol = Solution()

    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)

    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)

    c = result = sol.addTwoNumbers(list1, list2)  # 7 -> 0 -> 8
    while c:
        print(c, end=" -> ")
        c = c.next
