# Time Complexity: O(n), Space complexity: O(n)
class Solution:
    def rotationalCipher(self, input: str, rotation_factor: int) -> str:
        output = list(input)

        for i, c in enumerate(output):
            if c.isdigit():
                output[i] = str((int(c) + rotation_factor) % 10)
            elif c.isalpha():
                base = 97 if c.islower() else 65

                output[i] = chr(((ord(c) - base + rotation_factor) % 26) + base)

        return "".join(output)


if __name__ == "__main__":
    sol = Solution()
    assert sol.rotationalCipher("All-convoYs-9-be:Alert1.", 4) == "Epp-gsrzsCw-3-fi:Epivx5."
    assert sol.rotationalCipher("abcdZXYzxy-999.@", 200) == "stuvRPQrpq-999.@"
