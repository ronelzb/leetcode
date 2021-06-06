# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def convert_list_to_number(self, head: ListNode) -> int:
        num = 0
        move_to_left = 0
        while head:
            num += head.val * (10 ** move_to_left)
            move_to_left += 1
            head = head.next

        return num

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.convert_list_to_number(l1)
        num2 = self.convert_list_to_number(l2)
        result = num1 + num2

        if result == 0:
            return ListNode(0)

        # convert the number back to a reversed list
        head = tail = None
        while result:
            num = result % 10
            node = ListNode(num)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next

            result //= 10

        return head

    # Using only the lists to create a new list without converting to an int and back
    # Having the reversed nodes we can safely traversed both lists once
    # Where l1[0] and l2[0] are the least significant numbers respectively
    # When assigning carry to current get the least significant number as well to reverse the result
    def addTwoNumbers_efficient(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(0)
        carry = 0

        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
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

    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)

    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)
    sol.addToNumbers_efficient(head1, head2)  # [7, 0, 8]
