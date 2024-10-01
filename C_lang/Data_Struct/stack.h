#ifndef __STACK_H__
#define __STACK_H__
#include <stddef.h> /* size_t */

typedef struct stack_t stack_t;

stack_t *CreateStack (size_t capacity, size_t size_element);
void DestroyStack (stack_t *s);
void PopStack (stack_t *s);
void PushStack (stack_t *s, const void *element);
void *PeekStack (const stack_t *s);
size_t StackSize (const stack_t *s);
size_t StackCapacity (const stack_t *s);
int StackIsEmpty (const stack_t *s); /*return 1 if empty, otherwise 0 */

#endif /* __STACK_H__*/
