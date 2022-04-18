import random
k=0
set1={0}
set2={0}
print("",set1 ,"\n" , set2)
print(random.randrange(1,11))
while True:
    if k<=10:
        a1=random.randrange(1,11)
        print("a1=",a1)
        a2=random.randrange(1,11)
        print("a2=",a2)
        set1.add(a1)
        set2.add(a2)
        k=k+1
    else:
        set1.remove(0)
        set2.remove(0)
        print("set1=",set1)
        print("set2=",set2)
        break
print(set1.union(set2))
print(set1.difference(set2))






exit()
stl= {1,3,5,0}
stl2= {1,3,5,0}

stl.add(10)
stl.remove(10)
stl.discard(5)
print(stl==stl2)

print(stl)

set={1,3,4,9}
set2={6,32,7,}
print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))
print(set.clear())

