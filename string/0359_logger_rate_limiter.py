# https://leetcode.com/problems/logger-rate-limiter/
# tags: #design, #google, #hash_table
#
# Solution: Dictionary
# At the arrival of a new message we check if the message is eligible to be printed if
# * It hasn't seen before (does not exist in the dictionary).
# * We have seen the same message after 10 seconds.
# Time complexity: O(1), Space complexity: O(n)
class Logger:
    CACHE_MESSAGE_EXPIRATION = 10

    def __init__(self):
        self.cache = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.cache or timestamp - self.cache[message] >= self.CACHE_MESSAGE_EXPIRATION:
            self.cache[message] = timestamp
            return True

        return False


if __name__ == '__main__':
    logger = Logger()
    print(logger.shouldPrintMessage(1, "foo"))  # True
    print(logger.shouldPrintMessage(2, "bar"))  # True
    print(logger.shouldPrintMessage(3, "foo"))  # False
    print(logger.shouldPrintMessage(8, "bar"))  # False
    print(logger.shouldPrintMessage(10, "foo"))  # False
    print(logger.shouldPrintMessage(11, "foo"))  # True

