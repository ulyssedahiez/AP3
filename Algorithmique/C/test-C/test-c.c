#include <stdio.h>

int trr = 1;




int main()
{
    int a = 32; // valeur de a
    int* ptra = &a;//adresse de a ; ptr a est un pointeur
    int** ptraa = &ptra; 

    printf("%d, %p  \n\n", a, ptra); // on prend la valeur de l'adresse de a
    printf("%d", *ptra);  // ptra est un pointeur, on va chercher la valeur à cette adresse avec *
    printf("\n \n %d", **ptraa);
    /*int nbr1 = 2;
    int* nbr2 = &nbr1;
    int* nbr3 = *nbr2;
    printf("%i  \n", &nbr1);
    printf("%i  \n", nbr2);
    printf("%i",nbr3);
    printf("Hello, World!\n");*/
    return 0;
}