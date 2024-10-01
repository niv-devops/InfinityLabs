/* Functions that deal with standard input and output */
#include <stdio.h>

int main()
{
   // Q6
   printf("---------- Q6 ----------\n");
   unsigned int *ip = 0;
   float f = 3;
   float *fp = &f;
   ip = (unsigned int *) fp;
   printf("%p", ip);
   //ip=fp;
   printf("%u\n", *ip);
   
   // Q7
   printf("---------- Q7 ----------\n");
   int *p = (int*) 17;
   printf("%d\n", (int)(long)(p+4));
   
   // Q8
   printf("---------- Q8 ----------\n");
   size_t i = 3;
   size_t array[] = {0, 1, 2, 3, 4, 5};
   printf("%lu\n", i[array]);
   
   // Q9
   printf("---------- Q9 ----------\n");
   i = 3;
   size_t arr[] = {0, 1, 2, 3, 4};
   printf("%lu %lu %lu %lu %lu\n", arr[i], *(arr+i), *(i+arr), i[arr], ((size_t)3)[arr]);
   
   // Q10
   printf("---------- Q10 ----------\n"); 
   int arr1[10];
   printf("sizeof int array: %lu\n", sizeof(arr1));
   char arr2[2];
   printf("sizeof char array: %lu\n", sizeof(arr2));
   const char *str1 = "ab";
   printf("sizeof char pointer: %lu\n", sizeof(str1));
   const char str2[] = "cd";
   printf("sizeof string array: %lu\n", sizeof(str2));
   const char str3[] = {'e', 'f'};
   printf("sizeof string array: %lu\n", sizeof(str3));
   str1=str2;
   printf("str1: %s\n", str1);
   
   // Q11
   int a[100];
   i=0;
   while(i<100)
   {
      a[i]=0;
      ++i;
   }
   int *end = a+100;
   int *point = a;
   while(++point != end)
   {
      *point = 0;
   }
   
   // Q13
   const char * string1=NULL;  //0
   char const * string2;       //1 
   char * const string3=NULL;  //2
   char* string4=NULL;         //3
   char* const string5;        //4
   string1=string2;            //5
   string2=string3;            //6 
   string4=string3;            //7
   //string3=string4;          //8 Won't compile: string3 is const pointer
   string2=string4;            //9
   //string4=string2;          //10 Won't compile: can't assign const-var pointer to var pointer
   //string5=string4;          //11 Won't compile: string5 is const pointer
}
