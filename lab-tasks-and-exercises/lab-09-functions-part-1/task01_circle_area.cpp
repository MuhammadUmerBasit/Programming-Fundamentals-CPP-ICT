#include <iostream>
using namespace std;

float circarea(float radius); // Function prototype

int main()
{
	float a, area;
	
	cout << "Enter the value of radius : \n";
	cin >> a;
	
    circarea(a); // Function call

	return 0;
}

float circarea(float radius) // Function definition
{
	float area;
	area = 3.14159265359 * radius * radius;
	cout << "Area of circle of radius " << radius << " is : " << area;
	
	return area;
}
