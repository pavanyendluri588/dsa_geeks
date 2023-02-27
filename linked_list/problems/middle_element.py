class Node:
    def __init__(self,data=None,address=None):
        self.data=data
        self.address=address
class linked_list(Node):
    def __init__(self):
        self.head=None
        self.count=0
    def insert(self,data1):
        self.count=self.count+1
        new_node=Node(data=data1)
        if self.head==None:
            self.head=new_node
            self.node_address=self.head
        else:
            self.node_address.address=new_node
        self.node_address=new_node
        """
            self.node_address=self.head
        while self.node_address!=None:
            self.node1_address=self.node_address
            self.node_address=self.node_address.address
        self.node1_address.address=new_node
        """
    def access(self):
        self.node_address1=self.head
        while self.node_address1!=None:
            print(self.node_address1.data)
            self.node_address1=self.node_address1.address
    def middle_element(self):
        if (self.count+1)%2==0:
           num=(self.count+1)/2
        else:
            num=(self.count+2)/2
        #print(self.count,num)
        count=0
        node_address=self.head
        while node_address!=None:
            count=count+1
            if count==num:
                print(node_address.data)
            node_address=node_address.address


obj=linked_list()
obj.insert(5)
#obj.insert(4)
#obj.insert(3)
#obj.insert(2)
#obj.insert(1)
obj.access()
print("=======================")
obj.middle_element()
