/* Functions that deal with standard input and output */
#include <stdio.h>

long l = 8;
long *foo(){ return &1; }

int main()
{
	*(foo()) = 5;
	
	printf("%ld\n", l);
	
	return 0;
}
