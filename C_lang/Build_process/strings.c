/* Functions that deal with standard input and output */
#include <stdio.h>
/* macros, and various functions for performing general functions */
#include <stdlib.h>
/* header to strings functions */
#include"hstrings.h"

/* Re-implementation of strlen from string.h
   strlen - calculate the length of a string,
   excluding the terminating null byte ('\0'). */
size_t StrLen(const char *s)
{
   size_t length = 0;
   while (*s != '\0')
   {
      length++;
      s++;
   }
   return length;
}

/* Re-implementation of strcmp from string.h
   strcmp - compare two strings:
   • 0, if s1 and s2 are equal
   • a negative value if s1 is less than s2
   • a positive value if s1 is greater than s2 */
int StrCmp(const char *s1, const char *s2)
{
   int sum1=0, sum2=0;
   
   while (*s1 != '\0')
   {
      sum1 += (int)*s1;
      s1++;
   }
   while (*s2 != '\0')
   {
      sum2 += (int)*s2;
      s2++;
   }
      
   return sum1-sum2;     
}
