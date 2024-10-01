/* For I/O like printf */
#include <stdio.h>
/* For NULL and exit macros */
#include <stdlib.h>

/* Exercise 1.a
void TwoDArr(int arr[row][col]); // regular 2D array
void TwoDArr(int rows, int cols, int arr[rows][cols]); // regular 2D array with args
void TwoDArr(int *arr[]); // array of pointers
void TwoDArr(int *arr, int rows, int cols); // array of pointers with args
void TwoDArr(int **arr); // double pointer
*/

/* Exercise 1.b */
void TwoDArr(int arr[3][5])
{
   arr[1][2] = 3; /* row 1, col 2 */
}

/* Exercise 1.c */
void ExC(int arr[3][5], int result[])
{
   int sum, row, col;
   
   for (row=0; row<3; row++)
   {
      sum = 0;
      
      for (col=0; col<5; col++)
      {
         sum += arr[row][col];
      }
      
      result[row] = sum;
   }
}

int main()
{
   int arr[3][5];
   int a[3][5] = { {1,1,1,1,1}, {1,3,5,7,9}, {0,2,4,6,8} };
   int result[3];
   int row, col;

   /* For exercise 1.b */
   printf("---------- Exercise 1.b ----------\n");
   
   TwoDArr(arr);
   
   for (row=0; row<3; row++)
   {
      for (col=0; col<5; col++)
      {
         printf("%d ", arr[row][col]);
      }
      printf("\n");
   }
   
   /* For exercise 1.c */
   printf("---------- Exercise 1.c ----------\n");
   
   ExC(a, result);
   
   for (row=0; row<3; row++)
   {  
      for (col=0; col<5; col++)
      {
         printf("%d ", a[row][col]);
      }
      printf("\n");
   }
   printf("sizeof array: %lu-Bits\n", sizeof(a));
   
   printf("results: ");
   for (row=0; row<3; row++)
   {
      printf("%d ", result[row]);   
   }
   printf("\n");
    
   return 0;
}
