class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def posto(node):
    if node is None:
        return

    stack1 = [node]
    stack2 = []

    while stack1:
        curr = stack1.pop()
        stack2.append(curr)

        if curr.left:
            stack1.append(curr.left)

        if curr.right:
            stack1.append(curr.right)

    while stack2:
        curr = stack2.pop()
        print(curr.data, end='')


# Create binary tree
r = Node(1)

r.left = Node(2)
r.right = Node(3)

r.left.left = Node(4)
r.left.right = Node(5)

r.right.left = Node(6)
r.right.right = Node(7)


# Call postorder traversal
posto(r)