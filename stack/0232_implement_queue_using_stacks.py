# https://leetcode.com/problems/implement-queue-using-stacks/
# tags: #design, #queue, #stacks
#
# Solution: 2 stacks
# Cracking the Interview Code problem 3.4
# Implement 2 stacks to achieve O(1) amortized time in pop/peek operations
# Amortized due we "refill" out_stack when is empty
# Time complexity:
# * Push: O(1)
# * Pop/Peek: O(1) amortized
# * Empty: O(1)
# Space complexity O(n)
from collections import deque


class MyQueue:
    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        if self.out_stack: return self.out_stack.pop()
        return None

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())  # 1
    print(q.pop())  # 1
    print(q.empty())  # False
