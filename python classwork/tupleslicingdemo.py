

#     0   1  2  3 4 5       6           7     8    9 0 1 2 3        +
t = (5.6,74,2.3,1,2,3,[544,987,364],"Python",False,0,0,1,1,True)
#     4   3  2  1 0 9       8          7      6    5 4 3 2  1       -


print(t[:])
print(t[:9])
print(t[3:])
print(t[2:12])
print(t[5:13:5])

print(t[::-1])
print(t[:-11])
print(t[-14::])
print(t[-7:-11])
print(t[-2:-10:-4])
