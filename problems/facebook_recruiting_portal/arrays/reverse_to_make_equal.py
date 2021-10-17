# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2869293499822992&ppid=454615229006519&practice_plan=0
# LeetCode: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
# My solution explained:
# https://github.com/ronelzb/leetcode/tree/master/array/1460_make_two_arrays_equal_by_reversing_sub_arrays.py
from collections import Counter, defaultdict
from typing import List


class Solution:
    def are_they_equal_sort(self, array_a: List[int], array_b: List[int]) -> bool:
        return sorted(array_a) == sorted(array_b)

    def are_they_equal_dict(self, array_a: List[int], array_b: List[int]) -> bool:
        indexes_counter = defaultdict(int)
        for i in range(len(array_a)):
            indexes_counter[array_a[i]] += 1
            indexes_counter[array_b[i]] -= 1

        for index in indexes_counter:
            if indexes_counter[index] != 0: return False

        return True

    def are_they_equal_counter(self, array_a: List[int], array_b: List[int]) -> bool:
        return Counter(array_a) == Counter(array_b)


if __name__ == "__main__":
    sol = Solution()
    print(sol.are_they_equal_sort(array_a=[1, 2, 3, 4], array_b=[1, 4, 3, 2]))  # True
