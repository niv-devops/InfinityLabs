/* For I/O like printf */
#include <stdio.h>
/* For NULL and exit macros */
#include <stdlib.h>
/* For string function like strlen */
#include <string.h>

void foo(int a[], int size)
{
   int i=0;
   
   for (i=0; i<size; i++)
   {
      a[i] = i*2;
   }
   
   /* printf("sizeof a: %lu\n", sizeof(a)); */
}

int main (void)
{
   char str[] = "welcome";
   int arr[10] = {0};

   /* For question 3 */
   char *p = "lalala";
   char array[10] = "lalala";
   
   foo(arr, 10);
   
   printf("sizeof str: %lu\n", sizeof(str));
   printf("sizeof arr: %lu\n", sizeof(arr));
   printf("str length: %lu\n", strlen(str));
   
   /* Question 3 */
   ++p; /* return first char +1 == 'a' */
   /* ++array; -- not possible, array is not pointer and its address cannoot be increased
     *p = 's'; -- changing address not possible, segmentation fault
     p[0] = 's'; -- same as above */
   array[1] = 's'; /* second char of array is now 's' */
   *(array+1) = 's'; /* same as above */
   1[array] = 's'; /* same as above */
        
   return 0;
}
