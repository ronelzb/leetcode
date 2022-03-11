# https://leetcode.com/problems/merge-sorted-array/
# tags: #array, #must_do_easy_questions, #sorting, #top_interview_questions, #two_pointers
#
# Solution: Two pointers
# The idea is to go from the last indexes of both arrays, compare and put elements from either A or B to
# the final position, which can easily get since we know that A have enough space to store them all and
# we know size of A and B
# Time complexity: O(max(m, n)), Space complexity O(1)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0

        for j in range(n):
            while i < m + j and nums2[j] > nums1[i]:
                i += 1

            nums1.insert(i, nums2[j])
            if i == m + j:
                break

        nums1[m + j + 1:] = nums2[j + 1:]


if __name__ == "__main__":
    sol = Solution()
    input_list = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1=input_list, m=3, nums2=[2, 5, 6], n=3)
    print(input_list)  # [1, 2, 2, 3, 5, 6]

    input_list = [4, 5, 6, 0, 0, 0]
    sol.merge(nums1=input_list, m=3, nums2=[1, 2, 3], n=3)
    print(input_list)  # [1, 2, 3, 4, 5, 6]

    input_list = [4, 0, 0, 0, 0, 0]
    sol.merge(nums1=input_list, m=1, nums2=[1, 2, 3, 5, 6], n=5)
    print(input_list)  # [1, 2, 3, 4, 5, 6]
