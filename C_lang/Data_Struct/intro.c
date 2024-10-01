#include <stdio.h> /* For printf */

void FindDup (int arr[], size_t size)
{
	int hash[100] = {0}; /* Limit number to 100 */
	size_t i = 0;

	puts("Duplicates in the array are: ");	
	for (i=0; i<size; ++i)
	{
		if (1 == hash[arr[i]])
		{
			printf("%d ", arr[i]);
		}
		else
		{
			hash[arr[i]] = 1;	
		}
	}
	puts("");
}

int main (void)
{
    int arr[] = {1, 3 ,5 ,3, 4, 8 ,5, 2, 2, 1, 4};
    size_t size = sizeof(arr) / sizeof(arr[0]);  
    FindDup(arr, size);	
	
	return 0;
}
