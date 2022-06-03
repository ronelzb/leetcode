# https://leetcode.com/problems/min-stack/
# tags: #design, #must_do_easy_questions, #stack, #top_interview_questions
#
# Solution: Stack + Dictionary
# This solution can be done with a tuple as well, we just need a way to store the current value along with the min
# at each stack item
# Time complexity: O(n), Space complexity O(n)
from collections import deque


class MinStack:
    def __init__(self):
        self.stack = deque()
        self.size = 0

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append({"min": min(self.stack[-1]["min"], val), "value": val})
        else:
            self.stack.append({"min": val, "value": val})

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]["value"]
        return 0

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1]["min"]
        return 0


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # return -3
    minStack.pop()
    print(minStack.top())  # return 0
    print(minStack.getMin())  # return -2
