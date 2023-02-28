class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left=left
        self.data=data
        self.right=right
class Tree:
    def insert(self,node=None,data=None):
        if node is None:
            return Node(data=data)
        if node.data > data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node
    def left_map(self,node=None):
        while node is not None:
            self.order_list.append(node)
            self.output_list.append(node)
            node=node.left
        self.pop_right_s4()
    def pop_right_s4(self,node=None):
        #pop list 
        a=self.order_list.pop()
        
        if a.right is not None:
            self.left_map(node=a.right)
        else:
            if len(self.order_list)>0:
                self.pop_right_s4()

    def pre_order_traversal(self,node=None):
        #step1
        #create a stack list 
        self.order_list=[]
        #create a output list
        self.output_list=[]

        self.left_map(node=node)

        #step2
        #assigning_to node
        #

        return self.output_list


tree=Tree()
root=tree.insert(data=40)
print("root:",root)
tree.insert(root,30)
tree.insert(root,25)
tree.insert(root,15)
tree.insert(root,28)
tree.insert(root,35)
tree.insert(root,50)
tree.insert(root,45)
tree.insert(root,60)
tree.insert(root,55)
tree.insert(root,70)
print("==============================")
list1=tree.pre_order_traversal(root)
print(list1)
print("===============================")
for i in list1:
    print(i.data,end=" ")