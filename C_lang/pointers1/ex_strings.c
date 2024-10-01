/* Functions that deal with standard input and output */
#include <stdio.h>
/* macros, and various functions for performing general functions */
#include <stdlib.h>

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

int StrCmp(const char *s1, const char *s2)
{
    while(*s1 && (*s1 == *s2))
    {
        s1++;
        s2++;
    }
    return *(const unsigned char*)s1 - *(const unsigned char*)s2;  
}

int main()
{
   char str1[] = "ad";
   char str2[] = "bc";
   
   printf("String 1 length: %lu\n", StrLen(str1));
   printf("String 2 length: %lu\n", StrLen(str2));
   printf("String compare: %d\n", StrCmp(str1, str2));
   return 0;
}
