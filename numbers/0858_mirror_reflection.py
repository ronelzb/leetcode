# https://leetcode.com/problems/mirror-reflection/
# tags: #math, #geometry
#
# Solution:
# https://leetcode.com/problems/mirror-reflection/discuss/2377070/Pseudocode-Explain-Why-Odd-and-Even-Matter
# https://leetcode.com/problems/mirror-reflection/discuss/939286/Mirror-Mirror-Flip-Flip-with-Pictures-%2B-10-lines-of-code-EVERYONE-CAN-UNDERSTAND!-YOU-TOO!
# Time complexity: O(n), Space complexity: O(1)
class Solution:
    def mirrorReflection(self, p, q):
        if q == 0:
            return 0

        height = q
        while height < p or height % p > 0:
            height += q

        up_flip = height / p
        right_flip = height / q
        top_corner = 1 if up_flip % 2 > 0 else 0

        return top_corner if right_flip % 2 > 0 else 2
