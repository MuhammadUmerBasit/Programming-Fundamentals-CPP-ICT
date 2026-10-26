#include <iostream>
using namespace std;

int absolute(int i); // Function prototype

int main()
{
	int number;
	int absolute_number;

	cout << "Enter an integer (positive or negative): ";
	cin >> number;
	
	absolute_number = absolute(number); // Function call
	cout << "The absolute value of " << number << " is " << absolute_number << endl;
	return 0;
}
int absolute(int i) // Function definition
{
	if( i >= 0)
		return i;
	else
		return -i;
}

