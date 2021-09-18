# https://leetcode.com/problems/expression-add-operators/
# tags: #backtracking, #dfs, #math, #string
#
# Solution 1: Backtracking & Evaluate Expression
# We use backtracking to generate all possible expressions by adding +, -, * to between the digits of s string.
# Then write a function eval(string expression) to evaluate a string expression,
# if the evaluated result is equal to target, we add that expression string to our answer.
# Time Complexity: O(4^n * n), Space complexity: O(3^n) due to recursive calls
#
# For the time complexity: On one call it goes with 1 and rest of the digits as 23 and
# in another call u go with 12 and the rest of the digits as 3, this 4th dimension of call is simulated by the for loop.
# so the complexity is O(4^n). Additional n is due to eval when i == n.
#
# Solution 2 (optimized): Backtracking & Evaluate on the fly
# Same step to use backtracking as solution 1, adding 2 new parameters into the method call current value and previous
# + and - operators are done as inferred, for previous + operator stays the same and - we flip it
# For * operator: To calculate the new result we need to minus prev then plus with prev * num.
# So newResult = value - prev + prev * num.
# Time Complexity: O(4^n), Space complexity: O(3^n) due to recursive calls
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtracking(i: int = 0, weave: str = "", value: int = 0, prev=None) -> None:
            if i == n and value == target:
                combinations.append(weave)
                return

            for j in range(i, n):
                sub_num = num[i: j + 1]
                tmp = int(sub_num)

                if j > i and num[i] == "0": break  # Skip leading zero number

                if i == 0:
                    backtracking(j + 1, sub_num, tmp, tmp)
                else:
                    backtracking(j + 1, weave + "+" + sub_num, value + tmp, tmp)
                    backtracking(j + 1, weave + "-" + sub_num, value - tmp, -tmp)
                    backtracking(j + 1, weave + "*" + sub_num, value - prev + prev*tmp, prev*tmp)

        n = len(num)
        combinations = []
        backtracking()
        return combinations


if __name__ == "__main__":
    sol = Solution()
    print(sol.addOperators(num="123", target=6))  # ["1*2*3","1+2+3"]
    print(sol.addOperators(num="105", target=5))  # ["1*0+5","10-5"]
