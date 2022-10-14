#include<stdio.h>
void main()
{
		int Phy,Chm,Bio,Hindi,English;
	float per;
	/* input marks of five subject */
	printf(" Enter five subjects marks:\n");
	
	printf("\nPhy Marks:");
	scanf("%d",&Phy);
	printf("\nChm Marks:");
	scanf("%d",&Chm);
	printf("\nBio Marks:");
	scanf("%d",&Bio);
	printf("\nHindi Marks:");
	scanf("%d",&Hindi),
	printf("\nEnglish Marks:");
	scanf("%d",&English);
	
	per=(Phy+Chm+Bio+Hindi+English)/5;
	printf("\npercentage=%.2f\n",per);
	 
    if(per>=75)
	{
		printf("distinction");
	}
	else if (per>=60)
	{
		printf("first class");
	}
	else if (per>=50)
	{
		printf("second class");
	}
	else if (per>=35)
	{
		printf("pass class");
	}
	else 
	{
		printf("fail");
	}
	
}