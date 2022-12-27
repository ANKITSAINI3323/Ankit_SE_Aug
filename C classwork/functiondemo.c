#include<stdio.h>
void func1();//function declaretion
void func2();
  
  
void main ()
{
	printf("\nIn main first : start");
	func1();//faction calling
	func2();
	printf("\nin main: end ");
	
	
}
void func1()
{
	printf("\nfunction 1 called");
	
}
void func2()
{
	printf("\nfunction 2 called");
	
}
