# https://leetcode.com/problems/wildcard-matching/
# tags: #dp, #greedy, #recursion, #string
#
# Solution 1: Dynamic Programming
# https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
# Time complexity: O(s*p), Space complexity: O(s*p)
#
# Solution 2: Simulation
# https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p%2Bs)-time
# Time Complexity: O(s*p), Space complexity: O(p)
#
# Solution 3: Greedy, One pass
# The basic idea is to have one pointer for the string and one pointer for the pattern. This algorithm iterates
# at most length(string) + length(pattern) times, for each iteration, at least one pointer advance one step.
# Explanation at:
# https://leetcode.com/problems/wildcard-matching/discuss/17810/Linear-runtime-and-constant-space-solution
# Time complexity: O(s+p), Space complexity: O(1)
class Solution:
    def isMatch_dp(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] != "*":
                break
            dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[m][n]

    def isMatch_simulation(self, s: str, p: str) -> bool:
        transfer = dict()
        state = 0

        for c in p:
            if c == "*":
                transfer[(state, c)] = state
            else:
                transfer[(state, c)] = state + 1
                state += 1

        goal = state
        states = {0}

        for c in s:
            # states = {transfer.get((at, token)) for at in states if at is not None for token in (c, "*", "?")}
            next_states = set()
            for token in (c, "*", "?"):
                for at in states:
                    next_state = transfer.get((at, token))
                    if next_state is not None:
                        next_states.add(next_state)

            states = next_states

        return goal in states

    def isMatch_greedy(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i, j, match, start = 0, 0, 0, -1

        while i < m:
            if j < n and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < n and p[j] == "*":
                match, start = i, j
                j += 1
            elif start > - 1:
                match += 1
                i, j = match, start + 1
            else:
                return False

        while j < n and p[j] == "*":
            j += 1

        return j == n


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch_greedy(s="aa", p="a"))  # False
    print(sol.isMatch_greedy(s="aa", p="*"))  # True
    print(sol.isMatch_greedy(s="cb", p="?a"))  # False
    print(sol.isMatch_greedy(s="adceb", p="*a*b"))  # True
    print(sol.isMatch_greedy(s="acdcb", p="a*c?b"))  # False

    print(sol.isMatch_greedy(s="", p="******"))  # True
