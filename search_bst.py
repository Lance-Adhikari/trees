class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


root = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)


# Search for 60 using the ordering of a binary search tree.
current = root

while current is not None:
    print("Checking:", current.key)

    if current.key == 60:
        print("Found!")
        break
    elif 60 < current.key:
        # Smaller values belong in the left subtree.
        current = current.left
    else:
        # Larger values belong in the right subtree.
        current = current.right
