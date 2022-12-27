#include<iostream>
using namespace std;
 


class A{
	public:
		
		void func();
		
};
 
void A::func()
{ 
    cout<<"this is function of class A";
    

}

int main() 
{
	A r;
	r.func();
	return 0;
}