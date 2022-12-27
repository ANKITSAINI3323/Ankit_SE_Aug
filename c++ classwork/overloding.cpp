#include<iostream>
using namespace std;

class MO
{
  public:
	int arithmetic( int a,int b)
	{ 
	  return a+b;
	}
	    
	
	int arithmetic( int a,int b,int c)
	{
		return a+b+c;
	}
};
int main (){
	
	MO m ;
   cout<<" add: "<<m.arithmetic( 1,5);
   cout<<" three add:"<<m.arithmetic(4,5,6);
	
	return 0; 
	
}