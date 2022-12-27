#include<stdio.h>
void main ()
{
	
	int i;
	int arr1[5],arr2[5];
	printf(" \nacccpeting array1 elements\n\n\n ");
	for(i=0;i<5;i++)
	
	{
		printf("enter elements %d :" ,i+1);
		scanf("%d",&arr1[i]);
		
	}
	printf("\ndisplying arry1 elements\n\n\n");
	for(i=0;i<5;i++)
	{
		printf("elments %d : %d\n",i+1,arr1[i]);
	}
	 
	printf("\n\n******************\n\n");
    printf("\nacccpeting array2 elements\n\n\n ");
	for(i=0;i<5;i++)
	
	{
		printf("enter element %d :" ,i+1);
		scanf("%d",&arr2[i]);
		
	}
	printf("\ndisplying array2 elements\n\n\n");
	for(i=0;i<5;i++)
	{
		printf("element %d : %d\n",i+1,arr2[i]);
	}
	
	
	
	printf("\n\n**************addition of 2 arrays *********\n\n");
	
	for(i=0;i<5;i++);
	{ 
	printf("element %d = %d\n",i+1,arr1[i] + arr2[i]);
	

	}
	
}

	
	


	



