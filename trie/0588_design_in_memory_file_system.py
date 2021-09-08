# https://leetcode.com/problems/design-in-memory-file-system/
# tags: #google, #trie
#
# TrieNode Implementation.
# Time Complexity:
# * ls: O(l + k*log(k)) l=path length / k=number of entries in the current directory
# * mkdir: O(l)
# * addContentToFile: O(l + c) c=new content length
# * readContentFromFile: O(l)
# Space complexity: O(n + s), n=number of dir dir/file nodes / s=total content size
from typing import List


class TrieNode:
    def __init__(self, content=None):
        self.children = dict()
        self.content = content


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        current = self.root
        paths = self.__path_split(path)

        for directory in paths:
            current = current.children[directory]

        if current.content is not None:
            return [current.content]
        else:
            return sorted(current.children.keys())

    def mkdir(self, path):
        """
        :type path: str
        :rtype: void
        """
        current = self.root
        paths = self.__path_split(path)

        for directory in paths:
            if directory not in current.children:
                current.children[directory] = TrieNode()
            current = current.children[directory]

    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: void
        """
        current = self.root
        paths = self.__path_split(filePath)

        for directory in paths:
            if directory not in current.children:
                current.children[directory] = TrieNode()
            current = current.children[directory]

        current.content = (current.content if current.content is not None else "") + content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        current = self.root
        paths = self.__path_split(filePath)

        for directory in paths:
            current = current.children[directory]

        return current.content

    @staticmethod
    def __path_split(path: str) -> List[str]:
        return path.split("/")[1:] if path != "/" else []


if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))  # []
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))  # ["a"]
    print(fs.readContentFromFile("/a/b/c/d"))  # "hello"
