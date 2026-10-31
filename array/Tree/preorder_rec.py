class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def preo(node):
    if node == None:
        return
    print(node.data,end=' ')
    preo(node.left)
    preo(node.right)

r=Node(1)
r.left=Node(2)
r.right=Node(3)

r.left.left=Node(4)
r.left.right=Node(5)

r.right.left=Node(6)
r.right.right=Node(7)
preo(r)


