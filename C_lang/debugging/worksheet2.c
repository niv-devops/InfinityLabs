/* Functions that deal with standard input and output */
#include <stdio.h>
/* macros, and various functions for performing general functions */
#include <stdlib.h>

static int s_i = 7; /* For Ex3 */

/* Ex1: Swaps two int */
void swap(int *a, int *b)
{
   int temp = *a;
   *a = *b;
   *b = temp;
}

/* Ex2: Copy an array */
void copy_array(int arr1[], int arr2[], int length)
{
   int i;
   for (i=0; i<length; i++)
   {
      arr2[i] = arr1[i];   
   }
}

/* Ex3: Swap two size_t and two *size_t */
void swap_sizet(size_t *st1, size_t *st2)
{
   size_t temp = *st1;
   *st1 = *st2;
   *st2 = temp;
}

int main()
{
   /* For Ex1 */
   int a=5, b=10;
   
   /* For Ex2 */
   int nums[] = {1, 3, 5, 7, 9};
   int length = sizeof(nums) / sizeof(nums[0]);
   int *copy = (int *) malloc(sizeof(int) * length);
   int i;
   
   /* For Ex3 */
   int *ptr = &i;
   int *ptr2 = (int *) malloc(sizeof(int));
   int **ptr3;
   
   /* For Ex4 */
   size_t st1=50, st2=100;
   
   printf("---------- Ex1 ----------\n"); 
   printf("Before swap: a=%d | b=%d\n", a, b);
   swap(&a, &b);
   printf("After swap: a=%d | b=%d\n", a, b);
   
   printf("---------- Ex2 ----------\n");
   copy_array(nums, copy, length);
   printf("Copied array: ");
   for (i=0; i<length; i++)
   {
      printf("%d ", copy[i]); 
   }
   printf("\n");
   free(copy);
   
   printf("---------- Ex3 ----------\n");
   if (ptr)
   {
      ptr3 = &ptr;
   }
   printf("Address of int: %p\n", (void *)&s_i);
   printf("Address of int pointer: %p\n", (void *)ptr);
   printf("Address of dynamically allocated int pointer 2: %p\n", (void *)ptr2);
   printf("Address of int pointer 3: %p\n", (void *)ptr3);
   free(ptr2);
   
   printf("---------- Ex4 ----------\n");
   printf("Before swap: a=%lu | b=%lu\n", st1, st2);
   swap_sizet(&st1, &st2);
   printf("After swap: a=%lu | b=%lu\n", st1, st2);
   
   return 0;
}
