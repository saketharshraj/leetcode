class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return 'Node(' + str(self.value) + ')'

def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)

def walk2(tree, stack):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            stack.append(node.left)
            stack.append(node.right)

mytree = Node(1, Node(2, Node(3), Node(4)), Node(5))
walk(mytree)