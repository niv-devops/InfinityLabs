/* Functions that deal with standard input and output */
#include <stdio.h>
/* macros, and various functions for performing general functions */
#include <stdlib.h>
 
int main()
{
   int *ptr = (int*) malloc(10 * sizeof(int)); /* For #1 */
   int arr[10]; /* For #2 */
   int num=10, num2=20; /* For #3 */
   int *pnum;
   
   arr[9] = 5; /* #1 */
   printf("%d\n", arr[9]);
   
   /* #3 */
   pnum = &num;
   free(ptr);
   *pnum = num2;
   
   /* #4 */
   if (ptr[1] == 5)
   {
      puts("ok");
   }
   
   return 0;
}
