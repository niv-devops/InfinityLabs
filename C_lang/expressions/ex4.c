/* Functions that deal with standard input and output */
#include <stdio.h>
/* Functions that deal with strings */
#include <string.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int var1, var2;
    
    printf("Enter first variable: \n");
    scanf("%d", &var1);
    
    printf("Enter second variable: \n");
    scanf("%d", &var2);
    
    printf("Original vars: var1 = %d | var2 = %d\n", var1, var2);
    swap(&var1, &var2);
    printf("Swaped vars: var1 = %d | var2 = %d\n", var1, var2);
    
    return 0;
}
