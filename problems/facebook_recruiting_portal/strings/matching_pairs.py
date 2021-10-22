# https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=559324704673058&c=896138004629128&ppid=454615229006519&practice_plan=0
# Two indices have to be swapped, regardless of which two it is, only one letter will remain the same.
# If i = 0 and j = 1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t
# Time Complexity: O(n), Space complexity: O(n)
class Solution:
    def matching_pairs(self, s: str, t: str) -> int:
        mismatch = set()
        matched = set()
        count, n = 0, len(s)
        dup = False
        for i in range(n):
            si, ti = s[i], t[i]
            if si == ti:
                count += 1
                if si in matched:
                    dup = True
                matched.add(si)
            else:
                mismatch.add(si + ti)

        if count == n:
            return n if dup else n - 2
        elif count == n - 1:
            unique_mismatch = mismatch.pop()
            if dup or unique_mismatch[0] in matched or unique_mismatch[1] in matched:
                return count
            return count - 1

        mismatch_s = set()
        mismatch_t = set()
        for um in mismatch:
            if um[1] + um[0] in mismatch:
                return count + 2
            elif um[1] in mismatch_s or um[0] in mismatch_t:
                return count + 1
            mismatch_s.add(um[0])
            mismatch_t.add(um[1])

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.matching_pairs(s="abcd", t="adcb"))  # 4
    print(sol.matching_pairs(s="abc", t="abc"))  # 1
    print(sol.matching_pairs(s="abc", t="abx"))  # 1
    print(sol.matching_pairs(s="ax", t="ay"))  # 0
    print(sol.matching_pairs(s="axb", t="axy"))  # 1
    print(sol.matching_pairs(s="axa", t="aya"))  # 2
    print(sol.matching_pairs(s="abx", t="abb"))  # 2
    print(sol.matching_pairs(s="abb", t="axb"))  # 2
    print(sol.matching_pairs(s="ax", t="ya"))  # 1
