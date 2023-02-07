"""
    WAP in Python to print No.s between 2000 to 3000 display only nos.
    where all 4 digits should be even nos. and not odd nos using list.
"""

"""
l=[]

for i in range(3333,3999):
    s = str(i)
    #print(type(s))
    if int(s[0])%2!=0 and int(s[1])%2!=0 and int(s[2])%2!=0 and int(s[3])%2!=0:
        #print(type(s[0]))
        l.append(i)
    
print(l)
"""

l=[]

for i in range(2000,3001):
    if i%2==0:
        l.append(i)
        print(l)
    else:
        l.append(i)
        print(l)
    
#print(l)
