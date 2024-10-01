/* For I/O like printf, puts  */
#include <stdio.h>
/* For NULL and exit macros */
#include <stdlib.h>
 
int main (void)
{
   /* #1 */
   int *ptr = (int*) malloc(10 * sizeof(int));
   
   /* #2 */
   int arr[10];
   arr[10] = 5;
   
   /* #3 */
   int num=10; num2=20;
   int *pnum;
   pnum = &num;
   free(*pnum);
   *pnum = num2;
   
   /* #4 */
   if (ptr(1) == 5)
   {
      puts("ok");
   }
   
   return 0;
}

