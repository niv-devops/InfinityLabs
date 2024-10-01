/* Functions that deal with standard input and output */
#include <stdio.h>
/* macros, and various functions for performing general functions */
#include <stdlib.h>
/* header to strings functions */
#include"hstrings.h"

int main()
{
   char str1[] = "abcd";
   char str2[] = "abcde";
   
   printf("String 1 length: %lu\n", StrLen(str1));
   printf("String 2 length: %lu\n", StrLen(str2));
   printf("String compare: %d\n", StrCmp(str1, str2));
   return 0;
}
