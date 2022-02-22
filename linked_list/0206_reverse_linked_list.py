# https://leetcode.com/problems/reverse-linked-list/
# tags: #blind_75_must_do, #linked_list, #recursion, #top_interview_questions
#
# Solution: In-place iterative
# Graphical explanation at:
# https://leetcode.com/problems/reverse-linked-list/discuss/1449712/Easy-C%2B%2BJavaPythonJavaScript-Explained%2BAnimated
# Time complexity: O(n), Space complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current

        return prev


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    c = h
    for i in range(2, 6):
        c.next = ListNode(i)
        c = c.next

    h = sol.reverseList(h)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
