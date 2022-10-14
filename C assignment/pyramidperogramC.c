#include<stdio.h>
void main()
{
	int i,j,m;
	for(i=1;i<=5;i++)
	{
		for(m=1;m<=i;m++)
		{
			printf(" ");
		}
		for(j=i;j<=5;j++)
		{
			printf("*");
		}
		printf("\n");
	}
}