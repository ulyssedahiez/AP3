#include <stdio.h>

int main()
{
    int a;
    int b;
    printf("Calculatrice :\n\n");
    printf("Valeur de a : ");
    scanf("%d", &a);
    getchar();
    printf("Valeur de b : ");
    scanf("%d", &b);
    getchar();
    printf("Valeur de a + b : %d", a+b);
    return 0;
}




/*
• écrit « Calculatrice : » et saute 2 lignes...
• écrit « Valeur de a : » et saute 1 ligne
• attend l'appui d'une touche
• écrit « Valeur de b : » et saute 1 ligne
• attend l'appui d'une touche
• écrit « Valeur de a + b : »

*/