/* stdio required for all file related operations */
#include <stdio.h>

void Print (int num)
{
   printf("%d ", num);
}

struct print_me {
   int num;
   void (*ptr)(int);
};

int main() 
{
   int i=0;
   
	struct print_me arr[10];
	
	for (i=0; i<10; i++)
   {
      arr[i].num = i;
      arr[i].ptr = Print;
      arr[i].ptr(arr[i].num);
   }
	
	return 0;
}
