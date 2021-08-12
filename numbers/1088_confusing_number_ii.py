# https://leetcode.com/problems/confusing-number-ii/
# tags: #backtracking, #dfs, #google, #numbers
class Solution:
    # As the problem suggests, at each current number we need to check if the resulting number
    # is different than the original using the 180 degrees rule
    # To optimize the subsequent numbers search (backtracking) it is possible to make the next
    # confusing number using a default map with the formula: next = current_number * 10 + next_key
    # Time complexity: O(n / ?), Space complexity: O(5 + recursion tree)
    def confusingNumberII(self, n: int) -> int:
        valid_numbers = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        res = 0

        def backtracking(current) -> None:
            nonlocal res

            if is_confusing_number(current):
                res += 1

            for key in valid_numbers.keys():
                next_val = current * 10 + key

                if 0 < next_val < n:
                    backtracking(next_val)

        def is_confusing_number(current):
            orig = current
            confusing_num = 0
            while current > 0:
                confusing_num = confusing_num * 10 + valid_numbers[current % 10]
                current //= 10
            return orig != confusing_num

        backtracking(0)
        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.confusingNumberII(20))  # 6=[6,9,10,16,18,19]
