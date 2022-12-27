#include<stdio.h>
void main ()
{
	
	int i;
	int arr1[5];
	printf(" \nacccpeting array elements\n\n\n ");
	for(i=0;i<5;i++)
	
	{
		printf(" enter elements %d :" ,i+1);
		scanf("%d",&arr1[i]);
		
	}
	printf("\ndisply arry elements\n\n\n");
	for(i=0;i<5;i++)
	{
		printf(" elments %d : %d\n",i+1,arr1[i]);
	}
	
	
	
	
	
	
	
	
}