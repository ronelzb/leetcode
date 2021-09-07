# https://leetcode.com/problems/task-scheduler/
# tags: #array, #greedy, #hash_table, #sorting, #heap, #counting
#
# Overall explanation:
# https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
#
# Math drawing explanation:
# https://leetcode.com/problems/task-scheduler/discuss/719689/Draw-a-picture-to-intuitively-understand-the-math-solution
#
# Solution 1: Array and sorting
# (c[25] - 1) * (n + 1) + 25 - i  is frame size
# when inserting chars, the frame might be "burst", then tasks.length takes precedence
# when 25 - i > n, the frame is already full at construction, the following is still valid.
# Time complexity: O(n*log(n)), Space complexity: O(26) => O(1)
#
# Solution 2: Use heap
# To minimize code I used a counter and then get the most common element hits in the dictionary
# From there retrieved how many elements share that number of hits
# After we have inserted all tasks of frequency M - 1 (which clearly will not collide),
# other tasks of frequency lower than M - 1 will never have any task written collide with it's left-neighbor.
# Now, with our remaining tasks, say LL, we will insert in the 1st, N+1th, (and 2N+1th, 3N+1th, etc. if necessary)
# positions in schedule order.
# This partial schedule would have length L = (M-1) * (N+1) + Mct.
# Time Complexity: O(n*log(n)), Space complexity: O(c) <= O(26) then O(1) c=distinct letters in the input list
from typing import List
from collections import Counter


class Solution:
    def leastInterval_sort(self, tasks: List[str], n: int) -> int:
        counter = [0 for _ in range(26)]
        for t in tasks:
            counter[ord(t) - ord("A")] += 1
        counter.sort()

        i = 25
        while i >= 0 and counter[i] == counter[25]:
            i -= 1

        return max(len(tasks), (counter[25] - 1) * (n + 1) + 25 - i)

    def leastInterval_heap(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        m = task_counts.most_common(1)[0][1]
        mct = len([v for v in task_counts.values() if v == m])
        return max(len(tasks), (m - 1) * (n + 1) + mct)


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval_sort(tasks=["A", "A", "A", "B", "B", "B"], n=2))  # 8
    print(sol.leastInterval_sort(tasks=["A", "A", "A", "B", "B", "B"], n=0))  # 6
    print(sol.leastInterval_sort(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))  # 16
    print(sol.leastInterval_sort(tasks=["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n=2))  # 12
