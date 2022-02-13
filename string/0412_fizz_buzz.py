# https://leetcode.com/problems/fizz-buzz/
# tags: #math, #simulation, #string, #top_interview_questions
#
# Solution: Iterative
# Time complexity: O(n), Space complexity O(1)
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ["1"]
        for i in range(2, n + 1):
            current = ""
            if i % 3 == 0: current += "Fizz"
            if i % 5 == 0: current += "Buzz"
            if not current: current += str(i)
            res.append(current)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(n=3))  # ["1","2","Fizz"]
    print(sol.fizzBuzz(n=5))  # ["1","2","Fizz","4","Buzz"]
