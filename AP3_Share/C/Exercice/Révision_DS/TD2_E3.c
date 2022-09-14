#include <stdlib.h>
#include <stdio.h>


static void getMeanSum(int * tab, int longueur, int * moyenne, int * somme){
    int add = 0;
    for (int i = 0; i < longueur; i++){
        add +=tab[i];
    }    
    *somme = add;
    *moyenne = add/longueur;
}


int main(int argc, char **argv)
{
    int i[5] = {0, 2, 4, 6, 10};
    int moyenne;
    int somme;

    int longueur = sizeof(i) / sizeof(i[0]);
    getMeanSum(i, longueur, &moyenne, &somme);

    printf("La moyenne est %d et la somme est %d", moyenne, somme);
    return 0;
}