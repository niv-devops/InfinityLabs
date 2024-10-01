#include <stdio.h> /* For printf */
#include <stdlib.h> /* For malloc */
#include <assert.h> /* For assert macro */
#include <string.h> /* For memcpy */
#include "stack.h" /* For stack struct and functions */

struct stack_t {
	void *arr;
	size_t capacity;
	int top;
	size_t elemSize;
};

stack_t *CreateStack (size_t capacity, size_t elem_Size)
{
	stack_t *s = (stack_t *) malloc(sizeof(stack_t) + capacity * elem_Size);
	/*stack_t *s = (struct stack_t*) malloc(sizeof(stack_t));*/
	if (NULL == s)
	{
		puts("Stack's memory allocation failed.");
		exit (1);
	}
	/*s->arr = malloc(elem_Size*capacity);
	if (NULL == s->arr)
	{
		puts("Array's memory allocation failed.");
		exit (1);
	}*/
	
	s->arr = (char *)s + sizeof(stack_t);
	s->capacity = capacity;
	s->top = -1;
	s->elemSize = elem_Size;
	
	puts("Stack created successfully.");
	return s;
}

void DestroyStack (stack_t *s)
{
	/*free(s->arr);*/
	free(s);
	s = NULL;
	puts("Stack deleted successfully.");
}

void PopStack (stack_t *s)
{
	if (-1 == s->top)
	{  
		puts("Stack is empty - Can't pop.");
		/* assert(NULL == s); */	/* For testing */
    }
    else
    {
    	s->top--;
    }
}

void PushStack (stack_t *s, const void *element)
{
	if ((size_t)(s->top+1) == s->capacity)
	{  
		puts("Push failed - stack overflow.");
		/* assert(NULL == s); */	/* For testing */
	}
	else
	{
		memcpy((s->top+1) * s->elemSize + (char*)s->arr, element, s->elemSize);
		s->top++;
	}
}

void *PeekStack (const stack_t *s)
{
	void *peek = NULL;
	if (-1 == s->top)
	{  
		puts("Stack is empty.");  
    }
    else
    {
    	peek = (s->top) * s->elemSize + (char*)s->arr;
    }
    return peek;
}

size_t StackSize (const stack_t *s)
{
	return s->top+1;
}

size_t StackCapacity (const stack_t *s)
{
	return s->capacity;
}

int StackIsEmpty (const stack_t *s) /*return 1 if empty, otherwise 0 */
{
	return (-1 == s->top);
}
