#https://www.javatpoint.com/inorder-traversal
class Node:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right
class Tree:
    def create_node(self,data=None):
        return Node(data=data)
    def insert1(self,node=None,data=None):
        if node is None:
            return self.create_node(data=data)
        if node.data > data:
            node.left = self.insert(node.left,data)
            print(node.left)
        elif node.data< data:
            node.right = self.insert(node.right,data)
            print(node.right)
    #geeks
    def insert(self,node, data):
        root=node
        key=data
        if root is None:
            return Node(data=key)
        else:
            if root.data == key:
                return root
            elif root.data < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root
        
    def left_insertion_s3(self,node=None):
        while node is not None:
            print("left insertion while")
            print(self.stack1)
            print(node.data)
            self.stack1.append(node)
            node=node.left
        print(self.stack1)
        self.pop_on_stack_s4()

    def pop_on_stack_s4(self):
        print("pop main")
        #a
        
        a=self.stack1.pop()
        print(a.data)
        #b
        self.in_order_list.append(a)
        #c
        if a.right is not None:
            print("a.right:",a.right)
            self.left_insertion_s3(node=a.right)
        else:
            if len(self.stack1)>0:
                self.pop_on_stack_s4()

    def in_order_traversal(self,node=None):
        #step1
        self.in_order_list=[]
        self.stack1=[]
        #step2
        #we already assignrd to root
        #step3
        self.left_insertion_s3(node=root)
       
       
        return self.in_order_list

tree=Tree()
root=tree.create_node(data=40)
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
list1=tree.in_order_traversal(root)
print("==============================")
for i in list1:
    print(i.data,end=" ")