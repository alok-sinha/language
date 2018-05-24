
#include <iostream>
using namespace std;
/*
 *  Arrays
 *  -> not a new type, but they hold numtiple of type. There is no generic array type, it is always array of somt type.
 *  -> but sizeof operator will return the whole space occupied by array in bytes
 *  -> Array init size : In C++ it must be constant or constant expression that is evaluated at compile time. In C, it can be expression for array on stack after 1999 standard. Note however that C++ has GNU extension that may allow epressions like C.
 */


/*** Array ***/
/**
 *  Partial array initialization will set the remaining elements to 0. This is true is there is member in {}. 
 *  @C_FEATURE : Supported
 *  @C++_FEATUREE : TBD
 *  @EXAMPLE
 *  @OUTPUT : 
 *    a[4]=0
 *    b[4]=0
 *. @ENDOUTPUT 
 */
void arrayInitWithLesserMember () {
	int a[10]={1,2};
	int b[10]={};

	cout << "a[4]=" << a[4] << endl;
	cout << "b[4]=" << b[4] << endl;

}

/*** End of Array */

/**
 *  Array initialization can be done without = sign. Keeping {} empty will set all the array members to 0. 
 *  @C_FEATURE : NotSupported
 *  @C++_FEATUREE : c++11
 *  @EXAMPLE
 */
void arrayInitWithoutEqual () {
	int a[10]={1,2};

	//cout << a[4] << endl;

}

/*** String ***/
/**
 *  getline functions to read string from standard input. Getline always reads upto n-1
 *  character. Onus is on user to make sure the passed char array has enough space. 
 *  getline will read upto n-1 chars or character input, whichever is earlier. 
 *  It also discards any newline char from input.
 *  
 *  @C_FEATURE : Supported
 *  @C++_FEATUREE : TBD
 *  @EXAMPLE
 *  @OUTPUT : 
 *    a[4]=0
 *    b[4]=0
 *. @ENDOUTPUT 
 */
void readInputUsingGetline (void) {
	char line[5];

	cin.getline(line,5);
	cout << "Line read =" << line <<endl;

	cin.getline(line,10);
	cout << "Line read =" << line <<endl;
}


/*** End of String */

void func (int & r) {

}
int main () {
	int x = 10;
	int & i = x;
	func(10);

	cout << i << endl;
	readInputUsingGetline();
}

/** => Pointers

=> Char arrays

=> Structurs and unions **/


