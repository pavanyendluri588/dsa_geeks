class Linked_List_Node:
    def __init__(self,address1=None,data1=None):
        self.data=data1
        self.address=address1
class Linked_List(Linked_List_Node):
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Linked_List_Node(data1=data)
        if self.head==None:
            self.head=new_node
            
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
            



class Doubly_LinkedList_Node():
    def __init__(self,previous_address=None,data=None,next_address=None):
        self.previous_address=previous_address
        self.data=data
        self.next_address=next_address
class Doubly_LinkedList(Doubly_LinkedList_Node):
    def __init__(self):
        self.head=None
        self.pre=None
    def Insert(self,data1):
        print("Inserting... {} in Doubly_LinkedList".format(data1))
        new_node=Doubly_LinkedList_Node(data=data1)
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

        


class circular_LinkedList_Node:
    def __init__(self,data=None,address=None):
         self.data=data
         self.address=address
class circular_LinkedList(circular_LinkedList_Node):
    def __init__(self):
        self.head=None
        self.new_address=None
    def insert(self,data1):
        new_node=circular_LinkedList_Node(data=data1)
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
            

            
        

        


        
        
