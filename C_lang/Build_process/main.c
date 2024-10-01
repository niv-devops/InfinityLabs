/* Function printf */
#include <stdio.h>
/* header to g file */
#include "g.h"

void foo (void);
int g_s = 3;

int main (void)
{
    printf("Value is: %d\n", g_s);
    foo();
    printf("Value is: %d\n", g_s);
    
    return 0;
}
