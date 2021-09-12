# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# tags: #graph, #heap, #shortest_path
#
# Solution: Dijkstra + Heap, explanation originally from @GraceMeng at LeetCode.
# The problem is to get maximum number of nodes I can reach from node 0 within M moves.
# Instead of maintaining a min-heap which keeps track of shortest distances to the source,
# we maintain a max-heap that keeps track of maximum moves remained for each node. Since:
# moves remained + distance from current node to source = M
# The bigger moves remained is, the smaller the distance will be.
# Thus, the max-heap can also promise the shortest distance.
#
# Time Complexity:
# * Dijkstra + Heap is O(E*log(E)), solution proposed below
# * Dijkstra + Fibonacci heap is O(V*log(V) + E)
# Space complexity: O(V^2)
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, sub_division in edges:
            graph[u][v] = graph[v][u] = sub_division
        heap_moves_remained = [(-maxMoves, 0)]
        seen = set()
        result = 0

        while heap_moves_remained:
            moves_remained, u = heapq.heappop(heap_moves_remained)
            moves_remained = -moves_remained
            if u not in seen:
                seen.add(u)
                result += 1
                for v in graph[u]:
                    if v not in seen and moves_remained >= graph[u][v] + 1:
                        heapq.heappush(heap_moves_remained, (-(moves_remained - graph[u][v] - 1), v))

                    move_cost = min(moves_remained, graph[u][v])
                    graph[v][u] -= move_cost
                    result += move_cost

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.reachableNodes(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3))  # 13
    print(sol.reachableNodes(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], maxMoves=10, n=4))  # 23
    print(sol.reachableNodes(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], maxMoves=17, n=5))  # 1
