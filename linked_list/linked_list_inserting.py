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
            
        while self.next_node_addr!=None:
            if self.next_node_addr.address==None:
                 break
            #print("self.next_node_addr:",self.next_node_addr,",self.next_node_addr.data:",self.next_node_addr.data,"self.next_node_addr.address:",self.next_node_addr.address)
            
            
            self.next_node_addr=self.next_node_addr.address
    def access_linked_list(self):
        self.addr=self.head
        while self.addr.address!=None:
            print("self.addr.data:",self.addr.data)
            self.addr=self.addr.address
    def insert_from_front_end(self,data):
        new_node =Node(data1=data)
        new_node.address=self.head
        self.head=new_node
    def insert_after_element(self,data,new_data):
        self.node_addr=self.head
        while self.node_addr!=None:
            if self.node_addr.data==data:
                new_node =Node(data1=new_data)
                
                new_node.address=self.node_addr.address
                self.node_addr.address=new_node
            self.node_addr=self.node_addr.address
    def insert_before_element(self,data,new_data):
        self.node_addr=self.head
        self.addr1=None
        while self.node_addr!=None:
             if self.node_addr.data==data:
                  self.addr1=self.node_addr
             self.node_addr=self.node_addr.address
        self.node_addr=self.head
        while self.node_addr!=None:
             if self.node_addr.address==self.addr1:
                   new_node =Node(data1=new_data)
                   self.node_addr.address=new_node
                   new_node.address=self.addr1
                   break
             self.node_addr=self.node_addr.address

    
    





        
         
        




obj=linkedlist()
for i in range(1,50,8):

    obj.insert_node(i)
obj.insert_from_front_end(99)
obj.insert_from_front_end(9999)
obj.insert_after_element(25,108)
obj.insert_before_element(25,111)
obj.access_linked_list()