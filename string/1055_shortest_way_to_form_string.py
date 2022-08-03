# https://leetcode.com/problems/shortest-way-to-form-string/
# tags: #dp, #google, #greedy, #string
#
# Solution: Dynamic Programming
# https://leetcode.com/problems/shortest-way-to-form-string/discuss/304662/Python-O(M-%2B-N*logM)-using-inverted-index-%2B-binary-search-(Similar-to-LC-792)
# Time complexity: O(m+n*log(m)) m=len(source) n=len(target), Space complexity: O(m)
import bisect
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        inverted_index = defaultdict(list)
        for i, c in enumerate(source):
            inverted_index[c].append(i)

        count = 1
        i = -1
        for c in target:
            if c not in inverted_index:
                return -1
            offset_list = inverted_index[c]
            j = bisect.bisect_left(offset_list, i)

            if j == len(offset_list):
                count += 1
                i = offset_list[0] + 1
            else:
                i = offset_list[j] + 1

        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestWay(source="abc", target="abcbc"))  # 2
    print(sol.shortestWay(source="abc", target="acdbc"))  # -1
    print(sol.shortestWay(source="xyz", target="xzyxz"))  # 3
