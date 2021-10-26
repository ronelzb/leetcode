# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=951929261870357&c=896138004629128&ppid=454615229006519&practice_plan=0
# This can be solved in log₂(logₘ(1000000000 / n))
#
# The only number in growthRates which we are interested are the largest numbers.
# As t increases, max(growthRates) ** t will be the largest term.
# First, search for all max(growthRates), this array is not larger than 1000.
#
# Let 'm' be the maximum number in growthRates.
# Let 'n' be the number of times 'm' appears in growthRates.
# Then we wish to find min(t) such that 1000000000 <= n * mᵗ.
#
# 1000000000 <= n * mᵗ
# 1000000000 / n <= mᵗ
# logₘ(1000000000 / n) <= t
#
# Therefore t is an upper bound to the solution.
# Now we perform binary search between 0 and t.
# Therefore the solution can be solved in log₂( logₘ(1000000000 / n) )
#
# Time Complexity: O(log(n)), Space complexity: O(1)
import math
from typing import List


class Solution:
    def getBillionUsersDay(self, growthRates: List[float]) -> int:
        def binary_search(left: int, right: int):
            if left == right: return right

            middle = (left + right) // 2
            total = sum(g ** middle for g in growthRates)
            if total < target:
                return binary_search(middle + 1, right)
            else:
                return binary_search(left, middle)

        target = 10 ** 9
        start = 1
        h = math.ceil(math.log(target, max(growthRates)))

        return binary_search(start, h)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getBillionUsersDay(growthRates=[1.1, 1.2, 1.3]))  # 79
    print(sol.getBillionUsersDay(growthRates=[1.01, 1.02]))  # 1047
