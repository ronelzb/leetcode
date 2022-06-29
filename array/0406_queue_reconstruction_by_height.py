# https://leetcode.com/problems/queue-reconstruction-by-height/
# tags: #array, #binary_indexed_tree, #greedy, #segment_tree, #sorting
#
# Solution: Greedy + Sorting
# https://leetcode.com/problems/queue-reconstruction-by-height/discuss/2211641/Visual-Explanation-or-JAVA-Greedy
# Time complexity: O(n*log(n)), Space complexity O(n)
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        people_ordered = []
        for h, k in people:
            people_ordered.insert(k, [h, k])
        return people_ordered


if __name__ == '__main__':
    sol = Solution()
    print(sol.reconstructQueue(
        people=[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]])
    )  # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
    print(sol.reconstructQueue(
        people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    )  # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
