#include <stdio.h>

int bar()
{
   printf("-1-");
   return 1;
}

int Fifi()
{
   printf("-2-");
   return 2;
}

int Dodo()
{
   printf("-3-");
   return 3;
}

void foo(int x, int y, int z)
{
   printf("%d %d %d\n", x, y, z);
}

int Mori (int x, int y)
{
   return x*4 + y*5;
}

int main()
{
   int i=1; i = ++i + 1;  //#1
   printf("i=%d\n", i); //expected 3
   
   int a=2, b=3, c; c = (a*b) + (++a + 4); //#2
   printf("a=%d | b=%d | c=%d\n", a, b, c); //expected 3 3 13
   
   foo(bar(), Fifi(), Dodo()); //#3
   //expected Dodo -> Fifi -> bar -> foo
   
   int j=2; int jj = Mori(++j, j); //#4
   printf("j=%d | jj=%d\n", j, jj); //expected 3 22 OR 3 27
   
   int e; float f=12.54; f=e=f*2; //#5
   printf("e=%d | f=%f\n", e, f); //expected 25 25.0
   
   double d=5; f=8/6; int h=12; unsigned int ui=2; //#6
   h = d/f + h*(ui-h);
   printf("h=%d\n", h); //expected -115
}
