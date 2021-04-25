from typing import List


# Boyer–Moore majority vote algorithm (https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter, current = 0, 0

        for i, num in enumerate(nums):
            if counter == 0:
                current = num
                counter = 1
            elif num == current:
                counter += 1
            else:
                counter -= 1

        return current


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(sol.majorityElement(nums))
