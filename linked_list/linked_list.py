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
        
         
        




obj=linkedlist()
for i in range(1,50,3):

    obj.insert_node(i)
obj.access_linked_list()