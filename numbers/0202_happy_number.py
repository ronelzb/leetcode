# https://leetcode.com/problems/happy-number/
# tags: #hash_table, #math, #top_interview_questions, #two_pointers
#
# Solution: Set
# For every new value, we check whether it is already in the set.
# Time complexity: O(n*log(n)), Space complexity: O(1)
#
# Other solutions: https://leetcode.com/problems/happy-number/discuss/57092/4-C%2B%2B-Solutions-with-Explanations
class Solution:
    def isHappy(self, n: int) -> bool:
        prev = set()

        while n > 1:
            if n in prev: return False
            prev.add(n)

            new_num = 0
            while n > 0:
                new_num += (n % 10) ** 2
                n //= 10

            n = new_num

        return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(n=19)
    assert not sol.isHappy(n=2)
