#include <iostream>
using namespace std;

enum eType {
    red=0,
    blue=1
};

int main() {
    eType e; /* Enum keyword is not needed for C++ */
    e = blue; /* You can not say e = 0, 1... */
    cout << e << endl;
    e = blue + 1;

    e = static_cast<eType>((int)3);

    return 0;
}