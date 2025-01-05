#include <stdio.h> /* For printf */

void Bursa (int stock_price[], int results[])
{
	int i=0;
	
	for (i=0; i<8; ++i)
	{
		if (stock_price[i] - stock_price[results[0]] > results[2])
        {
            results[1] = i;
            results[2] = stock_price[i] - stock_price[results[0]];
        }
        if (stock_price[i] < stock_price[results[0]])
        {
            results[0] = i;
        }
	}
}

int main (void)
{
	int stock_price[] = {6, 12, 3, 5, 1, 4, 9, 2};
	int results[3] = {0};
	
	results[0] = stock_price[0];
	results[1] = stock_price[1];
	results[2] = stock_price[1] - stock_price[0];
	
	Bursa(stock_price, results);
	
	printf("Buy at: %d\n", results[0]);
	printf("Sell at: %d\n", results[1]);
	printf("Profit is: %d\n", results[2]);
	
	return 0;
}
