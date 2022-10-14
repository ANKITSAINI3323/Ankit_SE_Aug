#include<stdio.h>
void main ()
{
	int count, t1=0,t2=1,n,i;
	printf("Enter the numbur of terms:");
	scanf("%d",&count);
	printf("%d t1 of fibonacci serise:\n",count);
	for(i=0;i<count;i++)
	{
	 	if(i<=1)
	 	 n=i;
	 	else
		 {
	 		n = t1+t2;
	 		t1=t2;
	 		t2=n;
	}
		  printf("%d\n",n);
	
    }
	
}
