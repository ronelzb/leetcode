# https://leetcode.com/problems/network-delay-time/
# tags: #bfs, #dfs, #graph, #heap, #shortest_path
#
# Solution: Dijkstra variant
# The idea is to use Dijkstra's shortest path algorithm to know the shortest time to reach all nodes and
# then chose the maximum time from all those shortest times,
# because it is this maximum time in which the signal would have received by all the nodes.
# Time complexity: O(V+E*log(V)), Space complexity: O(V+E)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        heap = [(0, k)]

        for x, y, w in times:
            graph[x].append((y, w))

        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)

            if len(visited) == n:
                return travel_time

            for neighbor, time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (travel_time + time, neighbor))

        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))  # 2
