#include<iostream>
using namespace std;

class A 
{
   	public:
   	int a;
   	void getA()
   	{
   		cout<<" Enter A ";
   		cin>>a;
   		
	   }
	   void showA()
	   {
	   	cout<<"A= "<<a;
	   	
	   }
};

 class B 
 {
   	public: 
   	int b;
   	void getB()
   	{
   		cout<<" Enter B ";
   		cin>>b;
	   }
   	void showB ()
   	{
   		cout<<"B"<<b;
	   }
	
};

int main()
{ 
    A a;
    a. getA();
	a. showA();
 
    B b;
    b.getB();
    b.showB();

	
	
	
}