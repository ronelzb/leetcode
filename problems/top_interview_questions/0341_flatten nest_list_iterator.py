# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = deque()
        for nestedInt in reversed(nestedList):
            self.stack.append(nestedInt)

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            current = self.stack[-1]
            if current.isInteger():
                return True
            self.stack.pop()
            for new_list in reversed(current.getList()):
                self.stack.append(new_list)

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
