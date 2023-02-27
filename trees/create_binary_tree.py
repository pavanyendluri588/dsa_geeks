class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right
class Tree:
    def Create_Node(self,data=None):
        return Node(data=data)
    def Insert(self,node=None,data=None):
        if node is None:
            return self.Create_Node(data=data)
        if node.data<data:
            node.left=self.Insert(node=node.left,data=data)
        elif node.data>data:
            node.right=self.Insert(node=node.right,data=data)
tree=Tree()
root=tree.Create_Node(data=5)
tree.Insert(root,1)
tree.Insert(root,2)
tree.Insert(root,5)
tree.Insert(root,9)
tree.Insert(root,41)
tree.Insert(root,14)
tree.Insert(root,42)
