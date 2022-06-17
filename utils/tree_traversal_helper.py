class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.val = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def __str__(self):
        return str(self.val)


def traverse_in_order(root):
    def traverse(current):
        if current.left:
            for left in traverse(current.left):
                yield left
        yield current
        if current.right:
            for right in traverse(current.right):
                yield right

    for node in traverse(root):
        yield node


if __name__ == '__main__':
    #   1
    #  / \
    # 2   3

    # in-order: 213
    # preorder: 123
    # postorder: 231

    bt = TreeNode(1,
                  TreeNode(2),
                  TreeNode(3))

    for n in traverse_in_order(bt):
        print(n.value)
