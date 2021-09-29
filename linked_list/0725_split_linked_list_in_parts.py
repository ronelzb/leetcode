# https://leetcode.com/problems/split-linked-list-in-parts/
# tags: #linked_list
#
# Solution: Two-pass
# First, find number of nodes n in our list and evaluate parts or cluster in which we will divide the nodes
# Also, the catch is to keep the leftover of the main division through modulo as we need to add at most 1
# additional node.
# If we are not at the None node (so, if part has at least one element),
# then we cut connection between current node and next one and go to the next node.
# Eventually, add the sub root found at the beginning of each iteration.
# Time Complexity: O(n + k), Space complexity: O(k)
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        cluster = n // k
        leftover = n % k
        current = head

        for i in range(k):
            root = prev = current

            for _ in range(cluster):
                prev, current = current, current.next

            if leftover > 0 and current:
                prev, current = current, current.next
                leftover -= 1

            if prev: prev.next = None
            res.append(root)

        return res


if __name__ == "__main__":
    sol = Solution()

    h = ListNode(1)
    h.next = ListNode(2)
    h.next.next = ListNode(3)
    array = sol.splitListToParts(head=h, k=5)  # [[1],[2],[3],[],[]]

    output = ""
    for h in array:
        output += ("," if output != "" else "") + "["

        c = h
        if c:
            while c:
                output += str(c) + " -> "
                c = c.next
        else:
            output += "None"

        output += "]"
    print(output)
