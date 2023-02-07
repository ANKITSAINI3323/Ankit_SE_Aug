"""
    List : It is a Collection type.

            It stores different types of values.
            It stores Duplicate values also.
            Insertion Order is maintain.
            Index starts with 0.
"""

l = [1,2,3,1.1,2.2,3.3,"Python",False,0,"Programming",1.1,True,2,3,1]

print(l)

l.append(100)
print(l)

l1 = l.copy()
print(l1)

l1.append(200)
print(l1)

l2 = l.copy()
print(l2)

l2.append(200)
print(l2)

l.pop()
print(l)

l2.pop()
print(l2)

print(l.count(1))
print(l.count(0))

l3 = [100,200,300]
l.extend(l3)
print(l)

print(l.index(1))
l.insert(0,"tops")
print(l)
l.insert(3,"Mohit")
print(l)
l.reverse()
print(l)

for i in range l :
    print(i)
    

























