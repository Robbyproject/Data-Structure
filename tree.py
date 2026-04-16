class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

class BinaryTree:
    def __init__(self):
        self.root=None

    def print_preorder(self,node):
        if node:
            print(node.value)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)


tree = BinaryTree()
tree.root = Node(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)

# tree2 = BinaryTree()
# subtree1 = Node(20)
# subtree1.left = Node(40)
# subtree1.right = Node(50)
# tree2.root.left = subtree1
# tree2.root.right = Node(30)

print("Preorder Traversal")
tree.print_preorder(tree.root)
print("Preorder Inorder")
tree.inorder(tree.root)
print("Preorder Postorder")
tree.postorder(tree.root)