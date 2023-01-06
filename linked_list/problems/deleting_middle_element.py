class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
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
            self.node_address.next=new_node
        self.node_address=new_node
    def access(self):
        new_address=self.head
        while new_address!=None:
            print(new_address.data)
            new_address=new_address.next
    def delete_middle(self):
        if self.count%2==0:
            num=(self.count/2)+1
        else:
            num=(self.count+1)/2
        self.new_address=self.head
        count=0
        check=0
        if self.count==1:
            self.head=None
            self.count=self.count-1
            check=1
        while self.new_address!=None and check==0:
            count=count+1
            if count==num-1:
                self.new_address.next=self.new_address.next.next
                check=1
                self.count=self.count-1
            else:
                self.new_address=self.new_address.next

        
obj=linked_list()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.access()
obj.delete_middle()
print("=====================")
obj.access()
