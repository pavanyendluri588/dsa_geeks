class Node:
    def __init__(self,data=None,address=None):
        self.data=data
        self.next=address
class linked_list(Node):
    def __init__(self):
        self.head=None
        self.count=0
    def insert(self,data1):
        self.count=self.count+1
        new_node=Node(data=data1)
        if self.head==None:
            self.head=new_node
            self.new_address=new_node
        else:
            self.new_address.next=new_node
        self.new_address=new_node
    def access(self):
        new_address=self.head
        while new_address!=None:
            print(new_address.data)
            new_address=new_address.next