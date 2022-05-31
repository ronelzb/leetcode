# https://leetcode.com/problems/merge-two-sorted-lists/
# tags: #bit_manipulation, #hash_table, #rolling_hash, #string
#
# Solution 1: Hash set
# We can count the number of combinations that can be formed of length k using input s and then compare it with
# the required number of combinations: 2^k
# Time complexity: O(n*k), Space complexity: O(n*k)
#
# Solution 1: Rolling hash
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/discuss/2092553/Explaining-the-Rolling-Hash-Method-or-Guide
# Time complexity: O(n), Space complexity: O(2^k)
class Solution:
    def hasAllCodes_set(self, s: str, k: int) -> bool:
        n, required_count = len(s), 2 ** k
        seen = set()

        for i in range(n - k + 1):
            temp = s[i:i+k]
            if temp not in seen:
                seen.add(temp)
                required_count -= 1
                if required_count == 0:
                    return True

        return False

    def hasAllCodes_rolling(self, s: str, k: int) -> bool:
        required_count, hash_code = 1 << k, 0
        seen = [0] * ((required_count - 1) // 32 + 1)
        mask = required_count - 1

        for i in range(len(s)):
            hash_code = ((hash_code << 1) & mask) | (int(s[i]))
            idx, bit_pos = hash_code // 32, hash_code % 32

            if i >= k - 1 and seen[idx] & (1 << bit_pos) == 0:
                seen[idx] |= (1 << bit_pos)
                required_count -= 1
                if required_count == 0:
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.hasAllCodes_rolling(s="00110110", k=2))  # True
