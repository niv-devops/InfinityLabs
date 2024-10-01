/* Functions that deal with standard input and output */
#include <stdio.h>

int main ()
{
    int n, i;
    float result=1.0;
        
    printf("Type a number: ");
    scanf("%d", &n);
    
    if (n>=0)
    {
        for (i=0; i<n; i++)
    	{
   	   result *= 10.0;
    	}
    }
    
    else
    {
        for (i=0; i>n; i--)
    	{
   	   result /= 10.0;
    	}
    }
    
    printf("Result: %f\n", result);
    
    return 0;
}
