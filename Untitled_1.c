#include <stdio.h>

int main(){char *s = "int main(){char *s = %c%s%c; printf(s, 34, s, 34, 10); %creturn 0;}"; printf(s, 34, s, 34, 10); return 0;}