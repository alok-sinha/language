#include <stdio.h>

enum eType {
    red,
    blue
};

int main() {
    /* Enum keyboard is needed for C */
    enum eType  e;
    e = red;
    e = 2;  /* Both form acceptable */


    /* How unions store data */
    union {
        int a;
        char s[13];
    } u = {"alok"};

    printf("Str : %d, %x", sizeof(u), u.a);
    return 0;
}