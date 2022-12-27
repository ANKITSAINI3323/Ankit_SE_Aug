#include<stdio.h>

void show( int *p)

{
	int i;
	printf("\npassing entire array in function using pointers:\n");
	for( i=0;i<5;i++)
	{
		printf("%d\t",*(p+i));
		
	}
}
void main ()
{
	int marks[5]={10,20,30,40,50};
	show(marks);
}