#include <stdio.h>
#include <stdlib.h>

struct stack {
	char par;
	struct stack* head;
};

void push(struct stack** head, int par);
int pop(struct stack** head);

int IsPair(char par1, char par2)
{
	if (par1 == '(' && par2 == ')')
	{
		return 1;	
	}
	else if (par1 == '{' && par2 == '}')
	{
		return 1;	
	}
	else if (par1 == '[' && par2 == ']')
	{
		return 1;
	}
	else
	{
		return 0;
	}
}

int IsBalanced(char exp[])
{
	int i = 0;
	struct stack* s = NULL;

	while (exp[i])
	{
		if (exp[i] == '{' || exp[i] == '(' || exp[i] == '[')
		{
			push(&s, exp[i]);
		}

		if (exp[i] == '}' || exp[i] == ')' || exp[i] == ']')
		{
			if (s == NULL)
			{
				return 0;
			}
			else if (!IsPair(pop(&s), exp[i]))
			{
				return 0;
			}
		}
		++i;
	}

	return (NULL == s);
}

int main (void)
{
	char exp[100] = "[()](){[()]()}";
	/* char exp[100] = "[{}(])"; */

	if (IsBalanced(exp))
	{
		puts("Balanced");
	}
	else
	{
		puts("Not Balanced");
	}
	return 0;
}

void push(struct stack** top, int par)
{
	struct stack* s = (struct stack*) malloc(sizeof(struct stack));

	if (NULL == s)
	{
		puts("Stack overflow.");
		getchar();
		exit(1);
	}

	s->par = par;
	s->head = (*top);
	(*top) = s;
}

int pop(struct stack** top)
{
	char par;
	struct stack* s;

	if (NULL == *top)
	{
		puts("Stack overflow.");
		getchar();
		exit(1);
	}
	else
	{
		s = *top;
		par = s->par;
		*top = s->head;
		free(s);
		return par;
	}
}
