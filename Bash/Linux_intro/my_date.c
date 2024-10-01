#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[], char *envp[])
{
   printf("Hello World\n");
   
   printf("you entered in reverse order:\n");

   while(argc--)
   {
      printf("%s\n",argv[argc]);
   }
   
   while(*envp)
      printf("%s\n",*envp++);

   return 0;
}
