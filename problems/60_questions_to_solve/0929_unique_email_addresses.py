# https://leetcode.com/problems/unique-email-addresses/
import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            m = re.search(r'^([^\+]*)\+?(.*)?@(.*)', email)
            if m:
                address = re.sub(r"\.", "", m[1])
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
