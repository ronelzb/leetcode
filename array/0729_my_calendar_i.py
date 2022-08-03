# https://leetcode.com/problems/my-calendar-i/
# tags: #binary_search, #design, #google, #ordered_set, #segment_tree
#
# Solution: Binary Search
# For each new interval, perform two binary searches:
# One to return the left index of start and one for the right index of end.
# Check if it has intersections with others.
# How we can check if we can insert new interval:
# 1. We need to make sure that t1 == t2, this is the condition where start and end are in the same gap.
# 2. t1 % 2 == 0, because it should be gap between two intervals.
# Time complexity: O(log(n)), Space complexity: O(n)
import bisect


class MyCalendar:
    def __init__(self):
        self.times = []

    def book(self, start: int, end: int) -> bool:
        t1 = bisect.bisect_right(self.times, start)
        t2 = bisect.bisect_left(self.times, end)

        if t1 == t2 and t1 % 2 == 0:
            self.times[t1: t1] = [start, end]
            return True

        return False


if __name__ == '__main__':
    calendar = MyCalendar()
    print(calendar.book(10, 20))  # True
    print(calendar.book(15, 25))  # False
    print(calendar.book(20, 30))  # True
