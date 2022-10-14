#include<stdio.h>
void main()
{
	int year;
	printf("Enter A year");
	scanf("%d",&year);
	//leap year if perfectly divisible by 400
	
	 if (year % 400 ==0)
	 {
	 printf("%d is a leap year",year);
     }
     //not a leap year if divisible by 400 
     //but not divisible by 400
     else if (year% 100==0)
     {
     	printf("%d is a not leap year",year);
	 }
     //leaf yearif not divisible by 100
     //but divisible by 4
     else if (year % 4==0)
     { 
     printf("%d is a leap year",year);
	 } 
     //all other years are not leap years 
     else
     {
     	printf("%d is not a leap yaer",year);
	}
     
}