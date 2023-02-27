class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right
class Tree:
    def create_node(self,data=None):
        return Node(data=data)
    def insert(self,node=None,data=None):
        if node is None:
            return self.create_node(data=data)
        if node.data < data:
            node.left = self.insert(node.left,data)
        elif node.data> data:
            node.right = self.insert(node.right,data)
tree=Tree()
root=tree.insert(data=5)
tree.insert(root,1)
tree.insert(root,13)
tree.insert(root,3)
tree.insert(root,15)
tree.insert(root,17)
tree.insert(root,12)
tree.insert(root,11)
tree.insert(root,18)
tree.insert(root,20)
tree.insert(root,17)
