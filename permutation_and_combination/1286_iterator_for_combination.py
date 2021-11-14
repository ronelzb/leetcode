# https://leetcode.com/problems/iterator-for-combination/
# tags: #backtracking, #bit_manipulation, #design, #iterator, #string
#
# Solution 1: Backtracking
# We can use a standard backtracking approach to generate all combinations.
# For each of characters in s, we can choose it, generate a combination string by recursive call to
# backtrack and backtrack by popping that character and try forming another combination by choosing the next one.
#
# In this case, since the string s is sorted and we are choosing characters 1-by-1 starting from 1st character in s,
# the backtrack will generate all strings in sorted order.
# So, we can simply store all the strings in an array and return one by one as per the calls we get.
# Time Complexity:
#   CombinationIterator: O(k!*k),
#   next: O(1)
#   hasNext: O(1)
# Total Space complexity: O(k!)
#
# Solution 2: Bit manipulation -> Gosper's hack
# Explanation at:
# https://leetcode.com/problems/iterator-for-combination/discuss/1576856/All-5-Solutions-w-Detailed-Explanations-or-Bitmask-%2B-Backtrack-%2B-On-The-Fly-%2B-Gosper's-Hack
# Time complexity:
#   CombinationIterator: O(n + k) => O(n),
#   next: O(n)
#   hasNext: O(1)
# Total Space complexity: O(1)




class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.index = 0
        self.combinations = []
        self.backtracking(characters, combinationLength, len(characters), "", 0)
        self.n = len(self.combinations)

    def backtracking(self, characters: str, combinationLength: int, n: int, weave: str, start: int) -> None:
        if len(weave) == combinationLength:
            self.combinations.append(weave)
            return None

        for i in range(start, n):
            self.backtracking(characters, combinationLength, n, weave + characters[i], i + 1)


    def next(self) -> str:
        if self.hasNext():
            temp, self.index = self.index, self.index + 1
            return self.combinations[temp]

    def hasNext(self) -> bool:
        return self.index < self.n


if __name__ == "__main__":
    sol = CombinationIterator("abc", 2)
    print(sol.next())  # "ab"
    print(sol.hasNext())  # True
    print(sol.next())  # "ac"
    print(sol.hasNext())  # True
    print(sol.next())  # "bc"
    print(sol.hasNext())  # False
