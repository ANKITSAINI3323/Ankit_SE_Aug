#include<stdio.h>
void main()
{
	float p,r,t;
	float Ci;
	
	printf("Enter the principal :");
	scanf("%f",&p);
	
	printf("\nEnter the rate : ");
	scanf("%f",&r);
	
	printf("\nEnter the time:");
	scanf("%f",&t);
	/*
	compound interest
	*/
	
	Ci=p*(pow((1+r/100),t));
	
	printf("compound interest %f\n",Ci);
	
	
	
	
}