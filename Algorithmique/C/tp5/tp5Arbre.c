#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct elements{
    int entier;
    struct element * droite;
    struct element * gauche;
};

typedef struct elements * element;

element newElement(int Entier) {
    element new = (element)malloc(sizeof(struct elements));
    new -> entier = (int *)calloc(4, sizeof(int));
    new -> entier = Entier;
    new->droite = NULL;
    new->gauche = NULL;
    return new;   
}

void construireArbre(element elemArbre, element elem){
    
}


int main(){

    return 0;
}