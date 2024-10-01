/* Functions that deal with standard input and output */
#include <stdio.h>

void Print(int a)
{
    printf("char is: %c\n", a);
}

int main (void)
{
    int a = 99;
    Print(a);
    Test(a);
    return 0;
}
