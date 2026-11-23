class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def height(node):
    # An empty tree has zero levels.
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    # Count this level plus the taller subtree.
    return 1 + max(left_height, right_height)


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)

print(height(root))
