# https://leetcode.com/problems/my-calendar-ii/
# tags: #binary_search, #design, #google, #segment_tree, #ordered_set
#
# Solution: Two lists
# https://leetcode.com/problems/my-calendar-ii/discuss/961691/Python-3-approaches-with-detailed-explanation
# Time complexity: O(n), Space complexity: O(n)

class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for i, j in self.overlaps:
            if start < j and end > i:
                return False

        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))

        self.calendar.append((start, end))

        return True
