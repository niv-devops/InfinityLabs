#include <stdio.h> /* For I/O like printf */
#include <stdlib.h> /* For NULL and exit macros */

int FindNextSoldierAlive (int index, int size)
{
	return (index+1) % size;
}

void JosephusProblem(int soldiers[], int size)
{
   int alive = size;
   int index=0;
   int i=0;

   while (1 != alive)
   {
      while (soldiers[index] == 0) /* Find next soldier alive */
      {
          index = FindNextSoldierAlive(index, size);
      }
      
      index = FindNextSoldierAlive(index, size); /* Give him the sword */

      while (soldiers[index] == 0) /* Find next soldier alive */
      {
         index = FindNextSoldierAlive(index, size);
      }

      soldiers[index] = 0; /* Stab him */
      alive--;
   } 

   for (i=0; i<size; ++i)
   {
      if (soldiers[i] == 1)
      {
         printf("Last man standing: #%d (soldier %d)\n", i, i+1);
         break;
      }
   }
}

int main (void)
{
   int size=0;
   int i=0;
   int *soldiers = NULL;
   
   puts("Enter amount of soldiers: ");
   scanf("%d", &size);
   
   while (size<1)
   {
      printf("Amount not valid!\n");
      puts("Enter amount of soldiers: ");
      scanf("%d", &size);
   }
   
   soldiers = (int*) malloc(size * sizeof(int));
   
   if (soldiers == NULL)
   { 
      printf("Memory not allocated.\n");
      exit(1);
   } 
   
   for (i=0; i<size; ++i)
   { 
      soldiers[i] = 1; 
   }
   
   JosephusProblem(soldiers, size);
   
   free(soldiers);
   return 0;
}
