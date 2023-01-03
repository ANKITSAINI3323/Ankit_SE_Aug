#perogam to disply the ficbonacci sequence up to n-the term 
nterms =int(input("how many term ?"))

#fitst two term 
n1, n2 = 0,1
count = 0

#chek if the number of terms is valid
if nterms <= 0:
    print("Plase enter the a postive nterms" )
    
#if there is only one term ,return n1
elif nterms == 1:
    print("Ficboncci sequence upto",nterms,":")
    print(n1)
    
else:
   print("ficboncc sequesce")
   while count < nterms:
       print(n1)
       nth = n1 + n2 
       n1 = n2 
       n2 = nth 
       count += 1
       
    