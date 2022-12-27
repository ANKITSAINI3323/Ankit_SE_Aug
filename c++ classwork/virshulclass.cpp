#include<iostream>
using namespace std ;

class A {
	public:
		void msg()
		{
			cout<<" hellow form class A";
			
	}
};
class B  : virtual public A {
	public :
		
};
 class C : virtual public B {
 	public :
 		
 };
class D :public B, public C{
	public:
		
};


int main (){
	 
	 D d;
	 d.msg();

	 return 0;

}