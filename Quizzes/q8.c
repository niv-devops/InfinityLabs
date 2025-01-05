/* For printf and puts*/
#include <stdio.h>
/* For size_t */
#include <stdlib.h>
/* For tolower function*/
#include <ctype.h>
#include <string.h>

void TF (int num)
{
	int i=1;
	for (i=1; i<num; ++i)
	{
		if (0 == i%3 && 0 == i%5)
		{
			printf("TF ");
			continue;
		}
		else if (0 == i%3)
		{
			printf("T ");
			continue;
		}
		else if (0 == i%5)
		{
			printf("F ");
			continue;
		}
		else
		{
			printf("%d ", i);
		}
	}
}

void RevLow (char *str, size_t size)
{
	size_t i=0;
	printf("Before reverse: %s\n", str);
    for (i=0; i<size/2; ++i)  
    {
    	char temp = str[i];  
        str[i] = str[size-i-1];  
        str[size-i-1] = temp;
        str[i] = tolower(str[i]);
    }
    for (i=0; i<size; ++i)  
    {
        str[i] = tolower(str[i]);
    } 
    printf("After reverse: %s\n", str);
}

int main (void)
{
	char string[] = "HelLowORLd";
	size_t size = strlen(string);
	
	TF(50);
	printf("\n");
	
	RevLow(string, size);
	return 0;
}
