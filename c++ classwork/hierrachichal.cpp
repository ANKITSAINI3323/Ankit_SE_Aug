#include<iostream>
using namespace std;
 
class side{ 
        public:
        int l;
		 void setVal( int x )
         {
         	l=x;
         	
		 }
};
class Square :public side{
	public:
		int square()
		{
			return l*l;
		}
};
class Cube:public side{
	public:
		int cube()
		{
			return l*l*l;
		}
};
int main()
{ 

	Square sq;
	sq.setVal(7);
	cout<<"\nSquare is : "<<sq.square();
	
	Cube c;
	c.setVal(4);
	cout<<"\nCube is : "<<c.cube();
	
}