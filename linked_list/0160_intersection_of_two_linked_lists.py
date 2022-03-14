# https://leetcode.com/problems/intersection-of-two-linked-lists/
# tags: #must_do_easy_questions, #top_interview_questions
#
# Solution: Length difference
# Calculate lengths of both lists and evaluate difference.
# Make this number of steps for the longest list, pointer p1 and pointer p2 put to start of short list.
# Move pointers p1 and p2 one by one until we have the same value:
# it will be either common element or it will be None element.
# Time complexity: O(m + n), Space complexity: O(1)
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
