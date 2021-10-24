# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=3068294883205371&c=896138004629128&ppid=454615229006519&practice_plan=0
# 1. Use a dict to store the count of each character under one node
# 2. A node's dict is the consolidated result of all its children + itself
# 3. Once the dict is built, traverse queries array and make lookup for each value in the map
# Time Complexity: O(n*q), Space complexity: O(n)
from collections import defaultdict
from typing import List


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

    def __str__(self):
        return str(self.val)


class Solution:
    def count_of_nodes(self, root: Node, queries: List[tuple], s) -> List[int]:
        def build_counter(node: Node) -> defaultdict:
            counter = defaultdict(int)
            counter[s[node.val - 1]] = 1

            for child in node.children:
                for key, val in build_counter(child).items():
                    counter[key] += val

            global_counter[node.val] = counter
            return counter

        result = []
        global_counter = dict()
        build_counter(root)

        for qi, qs in queries:
            result.append(global_counter[qi][qs])

        return result


if __name__ == "__main__":
    sol = Solution()

    root_1 = Node(1)
    root_1.children.append(Node(2))
    root_1.children.append(Node(3))

    print(sol.count_of_nodes(root=root_1, queries=[(1, 'a')], s="aba"))  # [2]

    root_2 = Node(1)
    root_2.children.append(Node(2))
    root_2.children.append(Node(3))
    root_2.children.append(Node(7))
    root_2.children[0].children.append(Node(4))
    root_2.children[0].children.append(Node(5))
    root_2.children[1].children.append(Node(6))

    print(sol.count_of_nodes(root=root_2, queries=[(1, 'a'), (2, 'b'), (3, 'a')], s="abaacab"))  # [4, 1, 2]
