class Solution:
    def roman_to_int(self, s: str) -> int:
        s_len = len(s)
        result = 0

        for i in reversed(range(s_len)):
            if s[i] == "I":
                if i + 1 < s_len and (s[i + 1] == "V" or s[i + 1] == "X"):
                    result -= 1
                else:
                    result += 1
            elif s[i] == "V":
                result += 5
            elif s[i] == "X":
                if i + 1 < s_len and (s[i + 1] == "L" or s[i + 1] == "C"):
                    result -= 10
                else:
                    result += 10
            elif s[i] == "L":
                result += 50
            elif s[i] == "C":
                if i + 1 < s_len and (s[i + 1] == "D" or s[i + 1] == "M"):
                    result -= 100
                else:
                    result += 100
            elif s[i] == "D":
                result += 500
            elif s[i] == "M":
                result += 1000

        return result


if __name__ == "__main__":
    sol = Solution()
    print("III >", sol.roman_to_int("III"))
    print("IV >", sol.roman_to_int("IV"))
    print("IX >", sol.roman_to_int("IX"))
    print("LVIII >", sol.roman_to_int("LVIII"))
    print("MCMXCIV >", sol.roman_to_int("MCMXCIV"))
