class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.s = [None] * 8  # storage list
        self.lf = float(2) / 3  # load factor
        self.DEFAULT_VALUE = "==TOMBSTONE=="

    def my_hash(self, key):  # can be modified to hash other hashable objects like built in python hash function
        return key % self.capacity

    def add(self, key: int) -> None:
        if float(self.size) / self.capacity >= self.lf:
            self.capacity <<= 1
            ns = [None] * self.capacity
            for i in range(self.capacity >> 1):
                if self.s[i] and self.s[i] != self.DEFAULT_VALUE:
                    n = self.my_hash(self.s[i])
                    while ns[n] is not None:
                        n = (5 * n + 1) % self.capacity
                    ns[n] = self.s[i]
            self.s = ns

        h = self.my_hash(key)

        while self.s[h] is not None:
            if self.s[h] == key:
                return
            h = (5 * h + 1) % self.capacity
            if self.s[h] == self.DEFAULT_VALUE:
                break

        self.s[h] = key
        self.size += 1

    def remove(self, key: int) -> None:
        h = self.my_hash(key)

        while self.s[h]:
            if self.s[h] == key:
                self.s[h] = self.DEFAULT_VALUE
                self.size -= 1
                return
            h = (5 * h + 1) % self.capacity

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        h = self.my_hash(key)
        while self.s[h] is not None:
            if self.s[h] == key:
                return True
            h = (5 * h + 1) % self.capacity
        return False


if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)  # set = [1]
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(1)  # return True
    assert not myHashSet.contains(3)  # return False, (not found)
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(2)  # return True
    myHashSet.remove(2)  # set = [1]
    assert not myHashSet.contains(2)  # return False, (already removed)
