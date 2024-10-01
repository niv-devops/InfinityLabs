/* For I/O like printf */
#include <stdio.h>
/* For datatype size_t and sizeof function */
#include <stdlib.h>

int main()
{
   printf("Data Type\tSize\n");
   printf("char\t\t%lu bytes\n", sizeof(char));
   printf("unsigned char\t%lu bytes\n", sizeof(unsigned char));
   printf("short\t\t%lu bytes\n", sizeof(short));
   printf("unsigned short\t%lu bytes\n", sizeof(unsigned short));
   printf("int\t\t%lu bytes\n", sizeof(int));
   printf("Unsigned int\t%lu bytes\n", sizeof(unsigned int));
   printf("long\t\t%lu bytes\n", sizeof(long));
   printf("unsigned long\t%lu bytes\n", sizeof(unsigned long));
   printf("float\t\t%lu bytes\n", sizeof(float));
   printf("double\t\t%lu bytes\n", sizeof(double));
   printf("long double\t%lu bytes\n", sizeof(long double));
   printf("pointer\t\t%lu bytes\n", sizeof(void*));

   return 0;
}
