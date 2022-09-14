#include <stdio.h>
#include <stdarg.h>
/*
void getAdress(int nb, ...){
    va_list ap;
    va_start(ap, nb); 
    int * n;
    int * lessAddress;
    while (nb > 0) {
        n = va_arg(ap, int*);
        printf("%p.\n", n);
        --nb; 
    }
    va_end(ap);
}
*/

void lowest(int nb, ...){
va_list ap;
va_start ( ap , nb );
int * n ;
int * lowest_ad = va_arg ( ap , int * );
while ( nb > 1) {
n = va_arg ( ap , int * );
//printf ("%p\n",n);
if(n < lowest_ad){
lowest_ad = n;
}
-- nb ;
}
va_end ( ap );
printf("adresse la plus faible: %p\n",lowest_ad);
}




int main(){
    int a = 0;
    printf("a  = %p.\n", &a);
    char * b = "bonjour";
    printf("b  = %p.\n", &b);
    double c = 3.5;
    printf("c  = %p.\n", &c);
    lowest(3 ,&a, &b, &c);
    return 0;
}