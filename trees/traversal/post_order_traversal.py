class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data= data
        self.right = right

class Tree:
    def insert(self,node=None,data=None):
        if node is None:
            return Node(data=data)
        if node.data>data:
            node.left = self.insert(node=node.left,data=data)
        elif node.data < data:
            node.right = self.insert(node=node.right,data=data)
        return node
    def left_order_s3(self,node=None):
        while node is not None:
            self.post_order_stack.append(node)
            node=node.left
    def pop_list_s4(self):
        
        a=self.post_order_stack.pop()
        self.output_list.append(a)
        if a.right is not None:
            self.left_order_s3(node=a.right)

    def post_order_traversal(self,node=None):
        #creating a post order stack 
        self.post_order_stack =[]

        #creating a output list 
        self.output_list=[]

        #step2 assigning  the node 
    
