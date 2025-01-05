#include <stdio.h> /* For printf */
#include <stddef.h> /* For size_t & sizeof */

void SortBinary (int arr[], size_t size)
{	
	int begin = 0; 
	int end = size - 1; 
  
	while (begin < end)
	{ 
		if (arr[begin] == 1)
		{ 
			if (arr[end] != 1)
			{
				arr[begin] = 0; 
				arr[end] = 1; 
			} 
			--end; 
		} 
		else
		{
			++begin;
		} 
	} 
}

int main (void)
{
	int arr[] = {1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0};
	size_t size = sizeof(arr) / sizeof(arr[0]);
	size_t i = 0;
	
	SortBinary(arr, size);
	
	for (i=0; i<size; ++i)
	{
		printf("%d ", arr[i]);
	}
	
	return 0;
}
