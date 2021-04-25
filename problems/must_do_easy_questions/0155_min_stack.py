class MinStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append({"value": val, "min": val})
        elif self.stack[-1]["min"] > val:
            self.stack.append({"value": val, "min": val})
        else:
            self.stack.append({"value": val, "min": self.stack[-1]["min"]})

        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            self.stack.pop()
            self.size -= 1

    def top(self) -> int:
        if self.size > 0:
            return self.stack[-1]["value"]
        return None

    def getMin(self) -> int:
        return self.stack[-1]["min"]


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
