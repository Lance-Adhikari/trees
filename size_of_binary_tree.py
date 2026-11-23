class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def size(node):
    # An empty subtree contains no nodes.
    if node is None:
        return 0

    left_size = size(node.left)
    right_size = size(node.right)

    # Count this node and all nodes in both subtrees.
    return 1 + left_size + right_size


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)

print(size(root))
