class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        l1=[data]
        self.stack=l1+self.stack
    def is_empty(self):
        if self.stack==[]:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty()==False:
            self.stack=self.stack[1:]
    def peek(self):
        if self.is_empty()==False:
            return self.stack[0]
        else:
            
            return None
    def access(self):
        for i in range(0,len(self.stack)):
            print(self.stack[i])
"""
obj=stack()
obj.push(10)
obj.push(100)
obj.push(1000)
obj.push(10000)
obj.push(100000)
obj.access()
obj.pop()
obj.access()
obj.peek()
print(obj.peek())
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.is_empty())
"""