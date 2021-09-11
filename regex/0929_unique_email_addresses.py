# https://leetcode.com/problems/unique-email-addresses/
# tags: #array, #hash_table, #regex, #string
#
# Solution 1: Use regex
# find valid emails using regex then separate the email user part to store it in a set, count the set
# Time complexity: O(n*m), Space complexity: O(n*m)
#
# Solution 2: Use string splitting only
# Instead of using regex make splitting to find the email address part required and store it in the set, count the set
# Time complexity: O(n*m), Space complexity: O(n*m)
import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            m = re.search(r'^([^\+]*)\+?(.*)?@(.*)', email)
            if m:
                address = re.sub(r"../problems/60_questions_to_solve", "", m[1])
                unique_emails.add(address + "@" + m[3])

        return len(unique_emails)

    def numUniqueEmailNoRegex(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            email_split = email.split("@")
            address_split = email_split[0].split("+")

            unique_emails.add("".join(address_split[0].split(".")) + "@" + email_split[1])

        return len(unique_emails)


if __name__ == "__main__":
    sol = Solution()

    assert sol.numUniqueEmailNoRegex(emails=
                        ["test.email+alex@leetcode.com",
                         "test.e.mail+bob.cathy@leetcode.com",
                         "testemail+david@lee.tcode.com"]) == 2
