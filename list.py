lst=[1,2,3]
print(lst)

lst1=[1,2,"harsha,2.3"]

#print list
print(lst1)

#negative index
print(lst1[-3])

#lists are nested
lst2=[[1,2,3],[4,5,6]]
print(lst2)

#lists are mutable
lst3=[1,2,3,4]
lst3[-2]=[5,6,7]
print(lst3)

#insert
lst4=[1,2,3,4]
lst4.insert(len(lst4),5)
lst4.insert(len(lst4),6)
print(lst4)

#append
lst4.append(7)
print(lst4)

#lists are dynamic
##means we can add and delete data