#include <stdio.h>

int main()
{
   
   if (-1 < (unsigned char)1)
   {
      printf("%x\n", (unsigned char)1);
      printf("A\n");
   }
   else
   {
      printf("b\n");
   }
   
   if (-1 < (unsigned int)1)
   {
      printf("%b\n", (unsigned int)1);
      printf("A\n");
   }
   else
   {
      printf("%b\n",  -1);
      printf("b\n");
   }
}
