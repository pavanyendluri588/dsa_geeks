class Node:
    def __init__(self,address1=None,data1=None):
        self.data=data1
        self.address=address1
class Linked_List(Node):
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data1=data)
        if self.head==None:
            self.head=new_node
            self.next_node=self.head
        else:
            self.next_node.address=new_node
        self.next_node=new_node
    def access(self):
        self.address11=self.head
        while self.address11!=None:
            print(self.address11.data)
            self.address11=self.address11.address
    def delete(self,data):
        self.node_addr=self.head
        count=1
        self.address=None
        if self.node_addr.data==data:
              self.head=self.node_addr.address
        if self.node_addr.address==None:
            self.head=None

        self.node_addr=self.head
        while self.node_addr!=None:
            if self.node_addr.data==data:
                self.address=self.node_addr.address
                break
            count=count+1
            self.node_addr=self.node_addr.address
        self.node_addr=self.head
        count=count-1
        count1=1
        while self.node_addr!=None:
            if count1==count:
                self.node_addr.address=self.address
            self.node_addr=self.node_addr.address
            count1=count1+1
    def delete_after(self,data):
        self.node_addr=self.head
        self.node_addr1=None
        while self.node_addr!=None:
            if self.node_addr.address!=None:
                self.node_addr1=self.node_addr.address
            if self.node_addr.data==data:
                self.node_addr.address=self.node_addr1.address
            self.node_addr=self.node_addr.address
        



        
    def delete_before(self,data):
        self.node_addr=self.head
        self.node_addr1=self.node_addr.address
        if self.node_addr1.data==data:
            self.head=self.node_addr.address

        self.node_addr=self.node_addr.address
        while self.node_addr!=None:
            break
    def bubble_sort_linked_list_by_data(self):
        self.node_addr_12=self.head
        count=0
        while self.node_addr_12!=None:
            count=count+1
            self.node_addr_12=self.node_addr_12.address
        self.node_addr_12=self.head
        for i in range(count):
            self.access()
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
    def bubble_sort_linked_list_by_address(self):
        self.node_addr_12=self.head
        count=0
        while self.node_addr_12!=None:
            count=count+1
            self.node_addr_12=self.node_addr_12.address
        self.node_addr_12=self.head
        for i in range(count):
            self.access()
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
    
 
                    


            



        
    

        

obj=Linked_List()
obj.insert(5555555)
obj.insert(555555)
obj.insert(55555)
obj.insert(5555)
obj.insert(555)
obj.insert(55)
obj.insert(5)
obj.insert(1)
obj.access()
obj.bubble_sort_linked_list_by_data()
obj.access()
obj.delete_after(5)
obj.delete(555)
obj.delete_after(55)
obj.access()
obj.bubble_sort_linked_list_by_data()



    