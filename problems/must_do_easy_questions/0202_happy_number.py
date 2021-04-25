class Solution:
    def isHappy(self, n: int) -> bool:
        previous_numbers = set()

        while n not in previous_numbers:
            previous_numbers.add(n)
            next_number = 0

            while n > 0:
                next_number += (n % 10) ** 2
                n //= 10

            if next_number == 1:
                return True
            n = next_number

        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(n=19)
    assert not sol.isHappy(n=2)
