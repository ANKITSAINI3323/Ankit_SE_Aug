#include<iostream>
using namespace std;

class Box
{    
double width, height,depth;

	public:
		
		Box()
		{
			cout<<"Default Constructor Called."	;
			width= 4;
			height=5;
			depth=6;
			
		}
		
		Box(double h,double w, double d)
		{
			cout<<"\nParameterized Constructor Called.";
			width=w;
			height=h;
			depth=d;
		}
		
		
		Box(const Box &obj)
		{
			cout<<"\nThis is Method";
			width=obj.width;
			height=obj.height;
			depth=obj.depth;
			
		}
	void volume()
	{
		cout<<" \n volume of box:"<<(width*height*depth );
	}
	
	
	
};

int main()
{
	Box b1;
	b1.volume();
	Box b2(7,8,9);
	b2.volume();
	Box b3(b1);
	b3.volume();
	
	
	
	
	
	
	
}