# https://leetcode.com/problems/sort-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    # Use bottom-up merge sort algorithm:
    # http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/merge-sort5.html
    # This code ensures time complexity: O(nlog(n)), space complexity: O(1)
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        def split(head, size):
            next_tail = head
            for _ in range(size - 1):
                if not next_tail:
                    return None
                next_tail = next_tail.next

            if not next_tail:
                return None
            next_head, next_tail.next = next_tail.next, None

            return next_head

        def merge(l, r, new_tail):
            while l and r:
                if l.val <= r.val:
                    new_tail.next = l
                    l = l.next
                else:
                    new_tail.next = r
                    r = r.next
                new_tail = new_tail.next

            new_tail.next = l or r
            while new_tail.next:
                new_tail = new_tail.next
            return new_tail

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        dummy = ListNode(next=head)
        step = 1
        while step < length:
            tail, current = dummy, dummy.next
            temp = current
            while temp:
                temp = temp.next

            while current:
                left = current
                right = split(left, step)
                current = split(right, step)
                tail = merge(left, right, tail)

            step *= 2

        return dummy.next


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(4)
    h.next = ListNode(2)
    h.next.next = ListNode(1)
    h.next.next.next = ListNode(3)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")

    h = sol.sortList(h)

    c = h
    while c:
        print(c, end=" -> ")
        c = c.next
    print("", end="\n")
