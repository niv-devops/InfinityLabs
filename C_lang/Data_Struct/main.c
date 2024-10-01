#include <stdio.h> /* For printf */
#include <stdlib.h> /* for free */
#include "stack.h" /* For stack struct and functions */

int main (void)
{
	stack_t *stack;
	size_t capacity = 0;
	size_t elemSize = sizeof(int);
	void *peek = NULL;
	int num1 = 5, num2 = 7;

	puts("Enter capacity of stack:");
	scanf("%lu", &capacity);
	
	stack = CreateStack(capacity, elemSize);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
		PopStack(stack);
	}
	
	puts("########## Pushing 1 out of 2 elements to stack ##########");
	PushStack(stack, &num1);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	
	puts("########## Pushing 2 out of 2 elements to stack ##########");
	PushStack(stack, &num2);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	
	puts("########## Pushing 3 out of 2 elements to stack ##########");
	PushStack(stack, &num2);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	
	puts("########## Poping second element from stack ##########");
	PopStack(stack);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
    
	puts("########## Poping first element from stack ##########");
	PopStack(stack);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	
	puts("########## Poping null element from stack ##########");
	PopStack(stack);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	puts("########## Destroy stack ##########");
	DestroyStack(stack);
	printf("1) Stack status: %d\n", StackIsEmpty(stack));
	printf("2) Stack capacity: %lu\n", StackCapacity(stack));
	printf("3) Stack size: %lu\n", StackSize(stack));
	peek = PeekStack(stack);
	if(NULL != peek)
	{
		printf("4) Top element is: %d\n", *(int *)peek);
	}
	
	return 0;
}
