
def test(a,b,c,*d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(10,20,30,40,50,60,70)


def test(a,b,c,*d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",list(d))

test(10,20,30,40,50,60,70)


def test(a,b,c,*d,**e):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",list(d),",E : ",e)

test(10,20,30,40,50,60,70,x=43,y=45,z=32,w=43)








