/* Functions that deal with standard input and output */
#include <stdio.h>

int main()
{
    int result = 0, n, digit;

    printf("Type a number: ");
    scanf("%d", &n);
    
    while (n>0)
    {
    	digit = n%10;
    	result = result*10 + digit;
    	n /= 10;
    }
    
    printf("Result: %d\n", result);
    
    return 0;
}
