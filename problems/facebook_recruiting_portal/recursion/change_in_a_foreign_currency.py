# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2903692913051025&c=896138004629128&ppid=454615229006519&practice_plan=0
# Time Complexity: O(n*k) k=targetMoney, Space complexity: O(n)
from typing import List


class Solution:
    def canGetExactChange(self, targetMoney: int, denominations: List[int]) -> bool:
        if not denominations: return False

        while denominations[-1] <= targetMoney:
            targetMoney -= denominations[-1]

        if targetMoney > 0:
            return self.canGetExactChange(targetMoney, denominations[:-1])

        return targetMoney == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.canGetExactChange(targetMoney=94, denominations=[5, 10, 25, 100, 200]))  # False
    print(sol.canGetExactChange(targetMoney=75, denominations=[4, 17, 29]))  # True
