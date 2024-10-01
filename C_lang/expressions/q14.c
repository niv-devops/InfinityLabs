#include <stdio.h>

int bar(int a, int b)
{
   printf("%d %d\n", a, b);
   return a*2 + b*3;
}

int main()
{
   int a=3, b=4, c, d; c = ++a; d = b++;
   printf("%d %d %d %d\n", a, b, c, d);
	
   if (a>b && b>2)
      printf("test");
      
   a = ++b + bar(++a, a+3);
   printf("%d\n", a);
}
