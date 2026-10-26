#include <iostream>
using namespace std;
int weight;				// Global Variable Declaration
int main()
{
 {
 double price = 2.0,	// Local variable declared and initialized
 height = 3.1,			// Local variable declared and initialized
 length = 2.4;			// Local variable declared and initialized
 cout << "Price is " << price << endl;
 cout << "Length is " << length << endl;
 cout << "Height is " << height << endl;
 }
 weight = 3;			// Global Variable Initialized Once
 cout << "Price is " << price << endl;		/* Here error is price, length, height; 
                                            because they are being used out of the scope; they are local variables. */
 cout << "Length is " << length<< endl;
 cout << "Height is " << height<< endl;

 return 0;
}
