class Node:
    def __init__(self,address1=None,data1=None):
        self.address = address1
        self.data= data1
    
class linkedlist(Node):
    def __init__(self):
        self.head=None
    def insert_node(self,data):
        new_node =Node(data1=data)
        if  self.head==None:
                self.head=new_node
                self.next_node_addr=self.head
        else:
            self.next_node_addr.address=new_node
        self.next_node_addr=new_node
    def access_linked_list(self):
        self.addr=self.head
        while self.addr.address!=None:
            print(self.addr,self.addr.data,self.addr.address)
            self.addr=self.addr.address

    def bubble_sort_linked_list(self):
        self.node_addr_12=self.head
        count=0
        while self.node_addr_12!=None:
            count=count+1
            self.node_addr_12=self.node_addr_12.address
        self.node_addr_12=self.head
        for i in range(count):
            print("==============")
            self.access_linked_list()
            self.node_addr_12=self.head
            while self.node_addr_12!=None and count>=2:
                #print(self.node_addr_12.address)
                #print(self.node_addr_12.address.address)
                #print("=======")
                if self.node_addr_12.address.address==None:
                    if self.node_addr_12.data>self.node_addr_12.address.data:
                        temp = self.node_addr_12.data
                        self.node_addr_12.data=self.node_addr_12.address.data
                        self.node_addr_12.address.data=temp
                    break

                else:
                    if self.node_addr_12.data>self.node_addr_12.address.data:
                        temp = self.node_addr_12.data
                        self.node_addr_12.data=self.node_addr_12.address.data
                        self.node_addr_12.address.data=temp
    
                self.node_addr_12=self.node_addr_12.address

         
        




obj=linkedlist()
"""
for i in range(1,50,3):

    obj.insert_node(i)
"""
obj.insert_node(122)
obj.insert_node(23)
obj.insert_node(3)
obj.insert_node(4)
obj.insert_node(13)
obj.insert_node(22)
obj.access_linked_list()
obj.bubble_sort_linked_list()
obj.access_linked_list()