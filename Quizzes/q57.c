#include <stdio.h>

int fibonacci(int index)
{
  if (index <= 0)
  {
    return 0;
  }
  else if (index == 1)
  {
    return 1;
  }
  else
  {
    return fibonacci(index-1) + fibonacci(index-2);
  }
}

int main()
{
  int index;

  printf("Enter an index for the Fibonacci sequence: ");
  scanf("%d", &index);

  int value = fibonacci(index);
  printf("Fibonacci(%d) = %d\n", index, value);

  return 0;
}
