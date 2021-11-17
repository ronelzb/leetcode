# https://leetcode.com/problems/restore-ip-addresses/
# tags: #backtracking, #dfs
#
# Solution: Backtracking
# Classical backtracking problem
# A valid IP address must be in the form of A.B.C.D,
# where A,B,C and D are numbers from 0-255.
# The numbers cannot be 0 prefixed unless they are 0.
# Time complexity: O(n!*n) where n=12 => O(1), Space complexity O(1)
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtracking(weave: List[int], start: int) -> None:
            if len(weave) == 4 and start == n:
                valid_ip_addresses.append(".".join([str(x) for x in weave]))

            for i in range(1, 4):
                if start + i <= n:
                    num = int(s[start:start + i])
                    if num <= 255:
                        backtracking(weave + [num], start + i)
                    if num == 0:
                        break

        n = len(s)
        valid_ip_addresses = []
        backtracking([], 0)
        return valid_ip_addresses


if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses(s="25525511135"))  # ["255.255.11.135","255.255.111.35"]
    print(sol.restoreIpAddresses(s="0000"))  # ["0.0.0.0"]
    print(sol.restoreIpAddresses(s="1111"))  # ["1.1.1.1"]
    print(sol.restoreIpAddresses(s="010010"))  # ["0.10.0.10","0.100.1.0"]
    print(sol.restoreIpAddresses(s="101023"))  # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
