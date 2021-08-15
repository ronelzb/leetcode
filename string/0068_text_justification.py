# https://leetcode.com/problems/text-justification/
# tags: #google, #greedy, #simulation, #string
from typing import List


class Solution:
    # Idea for the solution: The main method will manage how many words will fit in each line considering
    # at least one space between each word in the same line (greedy)
    # When a line is considered full, then fill in the line considering:
    # 1. If it's one word then it is easy, the result is just that word.
    # 2. If it's the last line then the result is all words separated by a single space
    # and filling remaining with blank space.
    # 3. Otherwise we calculate the size of each space evenly and if there is a remainder we distribute an extra space
    # until it is gone
    # Time complexity: O(n * maxWidth) => main method traverse words list and sub-method traverse the same list
    # Space complexity: O(maxWidth) => Space for a single line
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        text_lines = []
        n, current_width, line_start = len(words), 0, 0

        for i, word in enumerate(words):
            m = len(word)
            if current_width + m > maxWidth:
                text_lines.append(self.justify_line(words[line_start: i], current_width, maxWidth))
                line_start = i
                current_width = 0

            if i == n - 1:
                last_line = " ".join(words[line_start: i + 1])
                text_lines.append(last_line + " " * (maxWidth - len(last_line)))

            current_width += m + 1
        print(text_lines)
        return text_lines

    def justify_line(self, line_words: List[str], words_width: int, max_width: int) -> str:
        m = len(line_words)
        remaining = max_width - (words_width - m)
        if remaining == 0:
            return " ".join(line_words)
        elif m == 1:
            return line_words[0] + " " * (max_width - (words_width - 1))

        remaining_divisor = remaining // (m - 1)
        remaining_residual = remaining % (m - 1)
        text_line = ""

        for i, word in enumerate(line_words):
            divisor = ""
            if i > 0:
                divisor = " " * (remaining_divisor + (1 if remaining_residual > 0 else 0))
                remaining_residual -= 1 if remaining_residual > 0 else 0

            text_line += divisor + word

        return text_line


if __name__ == "__main__":
    sol = Solution()

    sol.fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
    # Output:
    # [
    #    "This    is    an",
    #    "example  of text",
    #    "justification.  "
    # ]

    sol.fullJustify(words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16)
    # [
    #   "What   must   be",
    #   "acknowledgment  ",
    #   "shall be        "
    # ]

    sol.fullJustify(
        words=["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
               "Art", "is", "everything", "else", "we", "do"], maxWidth=20)
    # [
    #   "Science  is  what we",
    #   "understand      well",
    #   "enough to explain to",
    #   "a  computer.  Art is",
    #   "everything  else  we",
    #   "do                  "
    # ]
