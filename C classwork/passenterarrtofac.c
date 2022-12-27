#include<stdio.h>
void show( int arr[])
{
	int i;
	for( i=0;i<5;i++)
	{
		printf("%d\t",arr[i]);
		
	}
}
void main ()
{
	int marks[5]={10,20,30,40,50};
	show(marks);
}