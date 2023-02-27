class queue():
    def __init__(self):
        self.queue=[]
    def Enqueue(self,data):
        self.queue=[data]+self.queue
    def Dequeue(self):
        if self.is_empty()==True:
            self.queue=[]
        elif len(self.queue)==1:
           self.queue=[]
        else:
            self.queue=self.queue[:len(self.queue)-1]
    def is_empty(self):
        if self.queue==[]:
            return True
        else:
            return False
    def front(self):
        if self.is_empty()==True:
            return None
        elif len(self.queue)==1:
            return self.queue[0]
        else:
            return self.queue[len(self.queue)-1]
    def access(self):
        for i in range(0,len(self.queue)):
            print(self.queue[i])

"""
obj=queue()
obj.Enqueue(2)
obj.Enqueue(3)
obj.Enqueue(4)
obj.Enqueue(5)
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.Dequeue()
obj.access()
"""

    
