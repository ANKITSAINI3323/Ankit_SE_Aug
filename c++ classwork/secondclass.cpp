#include<iostream>
using namespace std;

class A{ 
public:
	int a;
	
	 void getA() 
	 {
	 	cout<<"enter A =";
	 	cin>>a;
	 }
	 void showA()
	 {
	 	cout<<"\nA"<<a;
		  }	 
};
class B:public A{ 
public: 
	int b;
	void getB()
	 {
	 	cout<<"enter B =";
	 	cin>>b;
	 }
	 void showB()
	 {
	 	cout<<"\nB"<<a;
	 	
		  }	 
};
class C :public B
{ 
public:
	int c;
	
	 void getC() 
	 {
	 	cout<<"enter c =";
	 	cin>>c;
	 }
	 void showC()
	 {
	 	cout<<"\nC"<<a;
		  }	 
};

int main()
{
	C c;
	c.getA();
	c.getB();
	c.getC();
	
	c.showA();
	c.showB();
	c.showC();
	return 0;
	
}

