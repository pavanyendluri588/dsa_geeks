#tree is usedf to represent the data in the hgierarcy 
#tree is acyclic 
#the data which is having the hierarcy those are represented by the tree
#tree can grow top to botton in the data structure  
#flipping the realtime tree we will get the visiluation of ds tree
#parent node(imediate presessor of current node) 
#root node doesnot have any parent node 
#child node(imediate successor of current node)
#leaf node(external nodes)
#non leaf nodes():all nodes-leadnodes
#path:sequence of the consecutive(one after another) edges from the source node to destination node.
#edge :link between the two nodes
#edges are unidirectional but not biderectional.
 


#degree of the current node = no of childern
#degree of the tree= max(all nodes degrees list)  or maxmimum degree amoung all nodes.

#depth of the node = length of path from root to that node
#                     total edges from root node to the current node.

#height of the node = length of the path from the current node to the it's  leaf node. 
#                      if there is two paths means we will consider the longest path
#height of the tree = height of the root node 


#level of a node = depth of the node    
#level of the tree = height of the tree


#if i have n nodes in the tree , means  n nodes = (n-1) edges

#traversing(traveling across) i an tree id done by depth first search(DFS) and breadth first search(BFS)







#creating the tree node:
class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.data=data
        self.right=right

#testing the node 
root = Node(data=5)
root.left=Node(data=10)
root.right= Node(data=50)
print("root:",root,"\nroot.data:",root.data,"\nroot.left:",root.left,"\nroot.right:",root.right)
print("====================================================")
print("second node:root-->left_node:\nroot.left:",root.left,"\nsecond node data:root.left.data:",root.left.data,"\nroot.left.left:",root.left.left,"\nroot.left.right:",root.left.right)
print("====================================================")
print("Third node:root-->right_node:\nroot.right:",root.right,"\nThird node data:root.right.data:",root.right.data,"\nroot.right.left:",root.right.left,"\nroot.right.right:",root.right.right)





#creating tree class
class Tree:
   def __init__(self):
       self.root=None
   def create_node(self,data=None):
       return Node(data=data)
   def insert(self,node=None,data=None):
       if node == None:
            return self.create_node(data=data)
       if  data<node.data:
             node.left = self.insert(node=node.left,data=data)
       elif data>node.data:
             node.right= self.insert(node=node.right,data=data)
       print(node.left,node.data,node.right)

       
       

Tree=Tree()
root=Tree.create_node(data=5)
print("===================================================")
print(root.left,"root:",root,root.right)
print("===================================================")
Tree.insert(node=root,data=25)
print("===================================================")
Tree.insert(node=root,data=2)
print("===================================================")
Tree.insert(node=root,data=25)
print("==================================================")
Tree.insert(node=root,data=17)
print("===================================================")
Tree.insert(node=root,data=1)
print("===================================================")
Tree.insert(node=root,data=3)
print("===================================================")
Tree.insert(node=root,data=23)
print("===================================================")
Tree.insert(node=root,data=25)
print("===================================================")
Tree.insert(node=root,data=75)
print("===================================================")
Tree.insert(node=root,data=1)


















