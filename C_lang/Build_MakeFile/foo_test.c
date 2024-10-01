/* Function printf */
#include <stdio.h>
/* header to g file */
#include "foo.h"

void foo (void);

int g_bar = 3;

int main (void)
{
    printf("Value is: %d\n", g_bar);
    foo();
    printf("Value is: %d\n", g_bar);
    
    return 0;
}
