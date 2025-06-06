#enqueue-append
#dequeue-pop

queue=[]
queue.insert(0,10)
queue.insert(0,20)
queue.insert(0,30)
print(queue)
queue.pop()
print(queue)

queue2=[]
queue2.append(1)
queue2.append(2)
queue2.append(3)
queue2.pop(0)
print(queue2)




queue3=[]
def add(ele):
    queue3.insert(0,ele)

def remove():
    queue3.pop()

while True:
    print("enter a number")
    print("1.add")
    print("2.remove")
    choice=int(input())
    if choice==1:
        print("length of queue")
        length=int(input())
        print("what elements should be inserted")
        for i in range(length):
            ele=int(input())
            add(ele)
        break
    elif choice==2:
        remove()
        break
    else:
        print("select 1 or 2")
        break

print(queue3)



#with modules

import collections
queue4=collections.deque
o=queue4()
o.appendleft(10)
o.appendleft(20)
print(list(o))


#queue class
import queue
queue5=queue.Queue
o1=queue5()
o1.put(10)
print(list(o1.queue))




