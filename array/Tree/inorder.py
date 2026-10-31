class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ino(node):
    stack = []
    curr = node

    while curr is not None or stack:

        # Move to the leftmost node
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        # Visit the node
        curr = stack.pop()
        print(curr.data, end='-')

        # Move to the right subtree
        curr = curr.right


# Create binary tree
r = Node(1)

r.left = Node(2)
r.right = Node(3)

r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)


# Call inorder traversal
ino(r)