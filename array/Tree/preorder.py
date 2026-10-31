class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preo(node):
    if node is None:
        return

    stack = [node]

    while stack:
        curr = stack.pop()

        print(curr.data, end=" ")

        # Push right child first
        if curr.right:
            stack.append(curr.right)

        # Push left child second
        if curr.left:
            stack.append(curr.left)


# Create binary tree
r = Node(1)

r.left = Node(2)
r.right = Node(3)

r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)


# Call preorder traversal
print("Preorder Traversal:")
preo(r)