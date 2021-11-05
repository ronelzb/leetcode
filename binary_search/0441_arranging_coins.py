# https://leetcode.com/problems/arranging-coins/
# tags: #binary_search, #math
#
# Solution 1: Simulation
# Each time increment i and add it to sum
# Time complexity: O(n), Space complexity O(1)
#
# Solution 2: Binary Search
# All the steps will be 1 + 2 + 3 + ... + x <= n
# The formula of finding the sum is: (x(x+1))/2.
# So we check if the current mid is less or more than n and according to that continue our regular binary search.
# Time complexity: O(log(n)), Space complexity O(1)
class Solution:
    def arrangeCoins_sim(self, n: int) -> int:
        i, sum = 0, 0
        while sum <= n:
            i += 1
            sum += i
        return i - 1

    def arrangeCoins_bs(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            middle = (left + right) // 2
            current_sum = middle * (middle + 1) // 2

            if current_sum == n:
                return middle
            elif current_sum <= n:
                left = middle + 1
            else:
                right = middle - 1

        return left - 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.arrangeCoins_bs(n=5))  # 2
    print(sol.arrangeCoins_bs(n=8))  # 3
