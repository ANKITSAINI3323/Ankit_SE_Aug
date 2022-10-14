#include <stdio.h>
void main()
{
    int n,t, i,sum = 0,remainder;

    printf("Enter an integer: ");
    scanf("%d", &n);
    
     t = n;
     
    while ( t !=0)
	{
		remainder = t%10;
		sum =sum+remainder;
		t =t/10;
	}
    

    printf("Sum  of digits of %d = %d\n", n,sum);

}
