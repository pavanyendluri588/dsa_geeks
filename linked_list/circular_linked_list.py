class Node:
    def __init__(self,data=None,address=None):
         self.data=data
         self.address=address
class circular_LinkedList(Node):
    def __init__(self):
        self.head=None
        self.new_address=None
    def insert(self,data1):
        new_node=Node(data=data1)
        if self.head==None:
            self.head=new_node
            new_node.address=self.head
            self.new_address=new_node
        else:
            self.new_address.address=new_node
            new_node.address=self.head
            self.new_address=new_node
    def access(self):
        self.new_address1=self.head
        while self.new_address1.address!=self.head:
            print(self.new_address1.data,self.new_address1.address)
            self.new_address1=self.new_address1.address
            if self.new_address1.address==self.head:
                print(self.new_address1.data,self.new_address1.address)
    def delete(self,data11):
        self.new_address1=self.head
        self.new_address2=self.head
        count=0
        if self.new_address1.data==data11:
            self.head=self.new_address1.address
            count=1
        while count==1:
            while self.new_address2.address!=self.new_address1:
                self.new_address2=self.new_address2.address
            self.new_address2.address=self.head
            count=2
        while self.new_address1.address!=self.head and  count==0:
            if data11==self.new_address1.address.data and self.new_address1.address.address==self.head:
                self.new_address1.address=self.head
                self.new_address=self.new_address1
                count=1
            if data11==self.new_address1.address.data:
                self.new_address1.address=self.new_address1.address.address
                count=1
            self.new_address1=self.new_address1.address
            

            
        

        


        
        
"""
obj=circular_LinkedList()
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.insert(8)
obj.insert(9)
obj.insert(10)
obj.insert(11)
obj.insert(12)
print("==============================")
obj.access()
obj.delete(5)
print("==============================")
obj.access()
obj.delete(9)
print("==============================")
obj.access()
obj.delete(12)
print("==============================")
obj.access()
obj.insert(12)
print("==============================")
obj.access()
obj.delete(12)
obj.delete(11)
obj.delete(10)
print("==============================")
obj.access()
            
""" 