#using list

queue=[]
queue.append(20)
queue.append(10)
queue.sort()
queue.append(1)
queue.sort()
print(queue)

#but this is very inefficient way
#best way is to implement is usinfg binary heap
#using priority queue

import queue
queue1=queue.PriorityQueue
o1=queue1()
o1.put(1,"harsha")
o1.put(23,"nani")
o1.put(3,"teja")

print(list(o1.queue))
print(o1.get())
print(o1.get())

