class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_length(list_node: ListNode) -> int:
            if not list_node:
                return 0

            current = list_node
            count = 1

            while current:
                count += 1
                current = current.next

            return count

        length_a = get_length(headA)
        length_b = get_length(headB)
        delta = abs(length_a - length_b)

        shortest = headA if length_a < length_b else headB
        current_shortest = shortest
        longest = headA if current_shortest == headB else headB
        current_longest = longest

        for _ in range(delta):
            current_longest = current_longest.next

        while current_shortest and current_shortest is not current_longest:
            current_shortest = current_shortest.next
            current_longest = current_longest.next

        return current_shortest


if __name__ == "__main__":
    headA = ListNode(1)
    headA.next = ListNode(9)
    headA.next.next = ListNode(1)

    headB = ListNode(3)

    headC = ListNode(2)
    headC.next = ListNode(4)

    headA.next.next.next = headC
    headB.next = headC

    sol = Solution()
    print(sol.getIntersectionNode(headA, headB))
