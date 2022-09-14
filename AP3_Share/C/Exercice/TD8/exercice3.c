#include <stdarg.h>
#include <stdio.h>
void lowest(int nb, ...)
{
    va_list ap;
    va_start(ap, nb);
    float *n;
    float somme;
    while (nb > 0)
    {
        n = va_arg(ap, float *);
        //printf ("%p\n",n);
        somme += *n;
        --nb;
    }
    va_end(ap);
    printf("la somme des données entrées: %.2f\n", somme);
}
int main()
{
    float a = 5.2;
    float b = 25.5;
    float c = 8.4;
    lowest(3, &c, &b, &a);
    return 0;
}