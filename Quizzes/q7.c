#include <stdio.h> /* For printf */
#include <stdlib.h> /* For size_t and sizeof*/

/* Better implementation */
int FindSingle1 (int arr[], size_t length)
{
	int single=0;
	size_t i=0;
    for (i=0; i<length; ++i)
    {
        single ^= arr[i];
    }
    return single;
}

int FindSingle2 (int arr[], size_t length)
{
    int isDup = 0;
    size_t i=0, j=0;
    
    for (i=0; i<length; ++i)
    {
    	isDup = 0;
        for (j=1; j<length; ++j)
        {
            if (i!=j && arr[i] == arr[j])
            {
                isDup = 1;
                break;
            }
        }
        if (!isDup)
        {
            return arr[i];
        }
    }
    printf("Single number is: %d\n", arr[i]);
    return i;
}

int main (void)
{
    int arr[] = {1, 3 ,5 ,3, 4, 8 ,5, 2, 2, 1, 4};
    size_t length = sizeof(arr) / sizeof(arr[0]);  
    printf("Single number is: %d\n", FindSingle1(arr, length));
    printf("Single number is: %d\n", FindSingle2(arr, length));
    return 0;
}
