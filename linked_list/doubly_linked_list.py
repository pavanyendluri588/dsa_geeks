class Node():
    def __init__(self,previous_address=None,data=None,next_address=None):
        self.previous_address=previous_address
        self.data=data
        self.next_address=next_address
class Doubly_LinkedList(Node):
    def __init__(self):
        self.head=None
        self.pre=None
    def Insert(self,data1):
        print("Inserting... {} in Doubly_LinkedList".format(data1))
        new_node=Node(data=data1)
        if self.head==None and  self.pre==None:
            self.head=new_node
            self.pre=new_node
            new_node.previous_address=new_node
            self.new_next_address=self.head
        else:
            new_node.previous_address=self.new_next_address
            self.new_next_address.next_address=new_node
        self.main=new_node
        self.new_next_address=new_node
        """
        while self.new_next_address!=None:
            self.main=self.new_next_address
            self.new_next_address=self.new_next_address.next_address
        """
        #new_node.previous_address= self.main
    def Access(self):
        print("==================")
        print("Accessing......:")
        if self.head==None:
            print("Doubly_LinkedList is empty")
        else:
            print("DATA in Doubly_LinkedList:")
        self.new_address1=self.head
        while self.new_address1!=None:
            print(self.new_address1.previous_address,self.new_address1.data,self.new_address1.next_address)
            self.new_address1=self.new_address1.next_address
        
    def Search(self,data1):
        print("==================")
        print("Searching.....:")
        count=0
        self.new_address1=self.head
        while self.new_address1!=None:
            if self.new_address1.data==data1:
                 count=1
            self.new_address1=self.new_address1.next_address
        if count==1:
            print("Data {} is present in the Doubly_LinkedList".format(data1))
        else:
            print("Data {} is NOT present in the Doubly_LinkedList".format(data1))
        
    def BackTrack(self):
        print("==================")
        print("Backtracking.....:")
        self.new_prev_add=self.new_next_address
        self.bef_prev_add=None
        while self.new_prev_add!=self.bef_prev_add:
            print(self.new_prev_add.data)
            self.bef_prev_add=self.new_prev_add
            self.new_prev_add=self.new_prev_add.previous_address

            
    def Delete(self,data11):
        print("==================")
        print("Deleting.........:")
        self.new_prev_address1=self.head
        count=1
        if self.new_prev_address1!=None:
            if self.new_prev_address1.data==data11:
                 self.new_prev_address1.next_address.previous_address=self.new_prev_address1.next_address
                 self.head=self.new_prev_address1.next_address
                 print("Data {} is DELETED from Doubly_LinkedList".format(data11))
                 count=count+1
        while self.new_prev_address1!=None:
            if self.new_prev_address1.next_address==None and data11==self.new_prev_address1.data:
                self.new_next_address=self.new_prev_address1.previous_address
                self.new_prev_address1.previous_address.next_address=None
                print("Data {} is DELETED from Doubly_LinkedList".format(data11))
                count=count+1
                break
                


            if data11==self.new_prev_address1.data:
                self.new_prev_address1.next_address.previous_address=self.new_prev_address1.previous_address
                self.new_prev_address1.previous_address.next_address=self.new_prev_address1.next_address
                print("Data {} is DELETED from Doubly_LinkedList".format(data11))
                count=count+1
                break
            self.new_prev_address1=self.new_prev_address1.next_address
        if self.head==None:
            print("Doubly_LinkedList is empty")
        elif count==1 and self.head!=None:
            print("Data {} not present in the Doubly_LinkedList".format(data11))

        

        """
        count1=1
        self.new_prev_address1=self.head
        while self.new_prev_address1!=None:
            if count1==count-1:
                self.new_prev_address1.previous_address.next_address=self.new_prev_address1.next_address
                self.new_prev_address1.next_address.previous_address=self.new_prev_address1.previous_address
                break
            count1=count1+1
            self.new_prev_address1=self.new_prev_address1.next_address
        """

            




        


        
        

obj=Doubly_LinkedList()
obj.Insert(5)
obj.Insert("55")
obj.Insert(555)
obj.Insert(5555)
obj.Insert(55555)
obj.Insert(555555)
obj.Access()
print("==================")
obj.Delete("55")
obj.Delete(555547329)
obj.Delete(555555)
obj.Access()
obj.Insert(555555)
print("==================")
obj.Access()
print("==================")
obj.BackTrack()