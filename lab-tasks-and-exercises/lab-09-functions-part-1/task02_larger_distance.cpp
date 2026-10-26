#include <iostream>
using namespace std;
float largerDistance(float num1, float num2); // Function prototype
int main()
{	
    float a, b, large;
    cout<<"Enter first number:"; 
    cin>>a;
    
    cout<<"Enter second number:"; 
    cin>>b;
 

    large = largerDistance(a, b); // Function call
	cout<< large <<" is larger value.";
	return 0;
}

float largerDistance(float num1, float num2) // Function definition
{
   
    if(num1>num2)
    {

	return num1;
    }
    else
    {
    return num2;
	}
}
