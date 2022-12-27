#include<iostream>
using namespace std;
 
class side{ 
        public:
        int l;
		 void setval( int x )
         {
         	l=x;
         	
		 }
};
class square:public Side{
	public:
		int square()
		{
			return l*l;
		}
		
};
class cube:public side 
 {
	public:
		int cube()
		{
			return l*l*l;
			
		}
};
int main(){
	square sq;
	sq.square(5);
	cout<<" square is :"<<sq.square();
	
	
	cube c;
	c.cube(7);
	cout<<"cube is "<<c.cube();

	return 0;
}