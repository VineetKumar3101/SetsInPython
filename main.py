print('-----------------------------------------------------------')

#SETSINPTHYON

#CREATE A SET
s1={23,24,90,24,25,69,31}
print(s1)

print('-----------------------------------------------------------')

#create a empty set
s2=set()
print(type(s2))

print('-----------------------------------------------------------')

#CONVERT LIST INTO SET
s3=set([4,5,6,8])
print(s3)

print('-----------------------------------------------------------')

#list through variable
l1=[3,4,5,6,7,"Vineet"]
s4=set(l1)
print(s4)

print('-----------------------------------------------------------')

#add in set

s4.add(10)
print(s4)

print('-----------------------------------------------------------')

#update through list and set
s4.update([9,8],{23,45})
print(s4)

print('-----------------------------------------------------------')

#through Variables

s5={100,200}
s4.update(s5)
print(s4)

print('-----------------------------------------------------------')

#dicard or remove
s4.discard(23)
s4.remove(9)
print(s4)

print('-----------------------------------------------------------')

#clear the set
s1.clear()
print(s1)

print('-----------------------------------------------------------')

#delete entire set
del s1

print('-----------------------------------------------------------')

#Operations In SET

#UNIOIN , INTERSECTION , DIFFERENCE

#set1
s6={45,63,25,26,5,33,66,39,63,6,96,35,8,96,2,6}
print(s6)

#set2
s7={5,8,2,25,865,63,58,89,3369,5,56,8,45,556,2,56,25}
print(s7)

print('-----------------------------------------------------------')

#union
print(s6|s7)

print(s6.union(s7))

print('-----------------------------------------------------------')

#intersectiom

print(s6&s7)

print(s6.intersection(s7))

print('-----------------------------------------------------------')

#differnece

print(s6-s7)

print(s6.difference(s7))

print('-----------------------------------------------------------')

#symetric diifernce

print(s6^s7)

print(s6.symmetric_difference(s7))

print('-----------------------------------------------------------')

#sort elements
print(sorted(s6))

print('-----------------------------------------------------------')

#min
print(min(s6))
print(min(s7))

print('-----------------------------------------------------------')

#max
print(max(s6))
print(max(s7))


print('-----------------------------------------------------------')

#length
print(len(s6))
print(len(s7))

print('-----------------------------------------------------------')

#sum
print(sum(s6))
print(sum(s7))

print('-----------------------------------------------------------')

#set with boolean elements
s8={True,True,True}
s9={True,False,True,True}

print(all(s8))
print(all(s9))

print('-----------------------------------------------------------')

print(any(s8))
print(any(s9))

print('-----------------------------------------------------------')

#
s10={False,False,False}
print(any(s10))

print('-----------------------------------------------------------')