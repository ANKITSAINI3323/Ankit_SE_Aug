"""
    Tuple : Like List tuple also contains multiple group of data.

    In List,  we use  []
    But in Tuple , we use ()

    In List, you can change the value at Runtime

    In Tuple, you cannot change the value at Runtime.
    
"""
t = (1,2,3,1.1,2.2,3.3,"tops",False,"Python",[100,200],54,78,98,1,0,True)

print(t)
print(t.count(0))
print(t.index(False))
print(t[9])
t[9].append(300)
print(t[9])
print(len(t))

for i in t:
    print(i)

print(51 in t)


















