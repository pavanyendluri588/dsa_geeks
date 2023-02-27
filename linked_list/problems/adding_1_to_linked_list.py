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
    def adding_1(self):
        self.new_address1=self.head
        str1=""
        while self.new_address1!=None:
            str1=str1+str(self.new_address1.data)
            self.new_address1=self.new_address1.next
        data11=int(str1)+1
        head = self.linked_list_creation(data=data11)
        return head
    def reversing_adding_1(self):
        self.new_address1=self.head
        str1=""
        while self.new_address1!=None:
            str1=str1+str(self.new_address1.data)
            self.new_address1=self.new_address1.next
        data11=int(str1[::-1])+1
        head = self.linked_list_creation(data=data11)
        return head
    def linked_list_creation(self,data):
        obj1=linked_list()
        for i in str(data):
            obj1.insert(int(i))
        return obj1.head
    def access_from_head(self,head):
        new_address=head
        while new_address!=None:
            print(new_address.data)
            new_address=new_address.next



    
        
obj=linked_list()
obj.insert(1)
obj.insert(9)
obj.insert(9)
obj.insert(9)
obj.adding_1()
head1=obj.adding_1()
print(head1)
obj.access_from_head(head=head1)
head1=obj.reversing_adding_1()
print(head1)
obj.access_from_head(head=head1)



