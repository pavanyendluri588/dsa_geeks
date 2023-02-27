class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.data=data
        self.right=right
class Right_Skewed_Binary_Tree:
    def Create_Node(self,data=None):
        return Node(data=data)
    def Insert(self,node=None,data=None):
        while node.right is not None:
            node=node.right
        node.right=self.Create_Node(data=data)
    def Access(self,node=None):
        node1=node
        count=1
        print("============================================")
        while node1 is not None:
            print(" "*count,node1.data)
            print(" "*(count+1),chr(92))
            count=count+2
            node1=node1.right
        print("============================================")
        
tree=Right_Skewed_Binary_Tree()
root=tree.Create_Node(5)
tree.Insert(root,10)
tree.Insert(root,1)
tree.Insert(root,9)
tree.Insert(root,8)
tree.Insert(root,6)
tree.Insert(root,1)
tree.Insert(root,7)
tree.Insert(root,15)
tree.Insert(root,12)
tree.Insert(root,14)
tree.Insert(root,11)
tree.Insert(root,-1)
tree.Insert(root,-4)
tree.Access(root)
"""
============================================
  5
   \
    10
     \
      1
       \
        9   
         \
          8
           \
            6
             \
              1
               \
                7
                 \
                  15
                   \
                    12
                     \
                      14
                       \
                        11
                         \
                          -1
                           \
                            -4
                             \
============================================

"""

