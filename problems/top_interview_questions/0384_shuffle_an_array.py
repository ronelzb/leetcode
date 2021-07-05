# https://leetcode.com/problems/shuffle-an-array/
import random
from typing import List


# One solution: Knuth shuffle https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
# The solution presented in leetcode: https://leetcode.com/problems/shuffle-an-array/discuss/86006/simple-java-solution
# Workaround solution: Python hack using lambda functions
class Solution:
    def __init__(self, nums: List[int]):
        self.reset = lambda: nums
        self.shuffle = lambda: random.sample(nums, len(nums))

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.reset()

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return self.shuffle()


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
if __name__ == "__main__":
    sol = Solution([1, 2, 3])
    print(sol.reset())
    print(sol.shuffle())
    print(sol.shuffle())
    print(sol.reset())
