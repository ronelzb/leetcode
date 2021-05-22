# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.WILDCARD = "."
        self.END_OF_WORD = "#"

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            current.setdefault(c, dict())
            current = current[c]
        current[self.END_OF_WORD] = True

    def search(self, word: str) -> bool:
        n = len(word)

        def search_helper(i: int, current: dict) -> bool:
            if i == n:
                return self.END_OF_WORD in current

            c = word[i]
            if c == self.WILDCARD:
                for suffix in current:
                    if suffix != self.END_OF_WORD:
                        if search_helper(i + 1, current[suffix]):
                            return True
                return False
            else:
                if c not in current:
                    return False
                return search_helper(i + 1, current[c])

        return search_helper(0, self.root)


if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    print(wd.search("pad"))  # return False
    print(wd.search("bad"))  # return True
    print(wd.search(".ad"))  # return True
    print(wd.search("b.."))  # return True
    print(wd.search("..."))  # return True

    test = WordDictionary()
    test.addWord("a")
    test.addWord("ab")
    print(test.search(".."))  # return True
    print(test.search("a"))  # return True
    print(test.search("aa"))  # return False
    print(test.search("a"))  # return True
    print(test.search(".a"))  # return False
    print(test.search("a."))  # return False
