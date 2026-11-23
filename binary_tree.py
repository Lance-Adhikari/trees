class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Create a root with a left child and a right child.
root = Node(10)

root.left = Node(5)
root.right = Node(20)

print(root.key)
print(root.left.key)
print(root.right.key)
