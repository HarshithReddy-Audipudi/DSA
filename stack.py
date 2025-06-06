#user defined

#Operations
#1.push
#2.pop
#3.peek or top
#4.isEmpty

stack=[]
stack.append(10)
stack.append(20)
stack.pop()
print(stack)



#lets build a custom custom stack class

class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "stack is empty"
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "stack is empty"

    def is_empty(self):
        return len(self.items)==0
    
    def display(self):
        return self.items
        



s = Stack()
s.push(10)
s.push(20)
print("Top:", s.peek())      # Output: 20
print("Popped:", s.pop())    # Output: 20
print("Is Empty:", s.is_empty())  # Output: False
print("Stack:", s.display()) # Output: [10]



#we can create stack using methods as well
##1.collections library-#deque class
import collections
stack=collections.deque
s=stack()
s.append(1)
s.append(2)
print(list(s))

##2.queue-lifoqueue-by put and get methods
import queue
stack=queue.LifoQueue
s1=stack(3)
s1.put(10)
s1.put(20)
s1.put(30)
try:
    s1.put(40,timeout=2)
except queue.Full:
    print("its full")



