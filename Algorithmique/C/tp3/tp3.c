#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
struct etudiant{
    char * nom;
    char * promotion;
    int  note[10];
};
struct complexes{
    int partReel;
    int partComp;
};

typedef struct complexes * complexe;

complexe newComplexe(int PartieReel, int PartieComplexe) {
    complexe new = (complexe)malloc(sizeof(struct complexes));
    new -> partReel = (int *)calloc(4, sizeof(int));
    new -> partReel = PartieReel;
    new -> partComp = (int *)calloc(4, sizeof(int));
    new -> partComp = PartieComplexe;
        
    return new;   
}


int moyenneEt(int* tab){
    int *moyenne;
    int *somme;
    for (int i=0; i<10; i++){
        *somme += tab[i];
    }
    *moyenne = *somme/10;
    return *moyenne;
    }

void main(){

    srand(time(NULL));

    struct etudiant num1;
    num1.nom = "mael";
    num1.promotion = "AP3";


    for (int i=0; i<10;i++){
        num1.note[i] = rand()%21;
    }

    return;
}