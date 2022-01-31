# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# tags: #array, #binary_search, #binary_indexed_tree, #divide_and_conquer, #merge_sort, #ordered_set, #segment_tree
#
# Solution: Merge sort
# When we merge two descendingly sorted arrays, for the element in the left array,
# if it's larger than the first number in the right array, it means this left-array element is larger than
# the every element of the right array(since the right array is sorted).
# Then, we update our smaller number after self counts for this left array element by add the length of the right array
# Time complexity: O(n*log(n)), Space complexity O(n)
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeWithCount(indexed_nums) -> List[int]:
            if len(indexed_nums) == 1:
                return indexed_nums

            curr_stack = []
            left = mergeWithCount(indexed_nums[:len(indexed_nums) // 2])
            right = mergeWithCount(indexed_nums[len(indexed_nums) // 2:])

            while left and right:
                if left[0] > right[0]:
                    counts[left[0][1]] += len(right)
                    curr_stack.append(left.pop(0))
                else:
                    curr_stack.append(right.pop(0))

            if left:
                curr_stack.extend(left)
            else:
                curr_stack.extend(right)

            return curr_stack

        n = len(nums)
        counts = [0] * n
        mergeWithCount([(num, i) for (i, num) in enumerate(nums)])
        return counts


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSmaller(nums=[5, 2, 6, 1]))  # [2,1,1,0]
    print(sol.countSmaller(nums=[0, 0]))  # [0,0]
    print(sol.countSmaller(nums=[-1, -2]))  # [1,0]
