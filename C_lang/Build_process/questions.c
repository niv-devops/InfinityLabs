/* Functions that deal with standard input and output */
#include <stdio.h>
/* For using malloc */
#include <stdlib.h>

/* For question #16 */
void Foo ()
{
    char str1[20];
    char *str2 = malloc (sizeof(*str2) * 20);
    char *str3 = "whatever";
    char str4[] = "whatever";
    
    /* For question #17
    str3[1] = 'a';  -->   Will cause Ssegmentation fault */
    
    printf("%c | %c | %c | %c\n", str1[0], *str2, str3[1], *str4);
    printf("%d | %d | %d | %d\n", str1[0], *str2, str3[1], *str4);
     
    free(str2);
}

int main ()
{
    Foo();  
    return 0;
}

/* For question #17
   To make this program not to compile, we can:
   - Add syntax error, using undeclared var
   - Remove include directives
   - const char *str3 = "whatever"; 
*/
