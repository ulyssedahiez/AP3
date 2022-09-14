#include <stdio.h>
#include <stddef.h>
void resultEntier(int a, int b)
{
    int resultat = a / b;
    printf("%d/%d=%d\n", a, b, resultat);
}
void resultFloat(int a, int b)
{
    float a2 = (float)a;
    float b2 = (float)b;
    float resultat = a2 / b2;
    printf("%d/%d=%.2f\n", a, b, resultat);
}
static void (*affiche(int a, int b))(int)
{
    void (*fonction)(int, int);
    if (a % b == 0)
    {
        fonction = &resultEntier;
    }
    else
    {
        fonction = &resultFloat;
    }
    fonction(a, b);
}
int main(void)
{
    int a = 10;
    int b = 2;
    affiche(a, b);
    return 0;
}
