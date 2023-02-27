 
class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left =left
        self.data=data
        self.right=right
class Tree:
    def create_node(self,value):
        return Node(data=value)

obj=Tree()
element1=obj.create_node(5)
element2=obj.create_node(5)
element1.left=element2   
element3=obj.create_node(5)
element1.right=element3
element4=obj.create_node(5)

element5=obj.create_node(5)
element2.left=element4
element2.right=element5

element6=obj.create_node(5)
element7=obj.create_node(5)
element3.left=element6
element3.right=element7

print(__name__)