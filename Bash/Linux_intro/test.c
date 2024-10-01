#include <stdio.h>

void fault_func() {
   int *ptr = NULL;
   *ptr = 10;
}

int main() {
    fault_func();
    return 0;
}
