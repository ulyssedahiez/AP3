#include<stdio.h>
#include<stdlib.h>
#include<time.h>

 

struct structEtudiant {
    char nom[13];
    char* promo;
    int notes[10];
};

 

typedef struct structEtudiant etudiant;

 

etudiant createEtudiant() {
    //etudiant* newEtudiant = (etudiant)malloc(sizeof(struct structEtudiant));
    etudiant newEtudiant = { "etudiant " };

 

    char lettre = rand() % 26 + 'a';
    char lettre2 = rand() % 26 + 'a';
    char lettre3 = rand() % 26 + 'a';
    newEtudiant.nom[9] = lettre; newEtudiant.nom[10] = lettre2; newEtudiant.nom[11] = lettre3;

 

    newEtudiant.promo = "AP3";

 

    for (int i = 0; i < 10; i++) {
        newEtudiant.notes[i] = rand() % 20;
    }
    return newEtudiant;
}

 

float calcMoyenne(etudiant eleve) {
    int sousTotal = 0;
    for (int i = 0; i < 10; i++) {
        sousTotal = sousTotal + eleve.notes[i];
    }
    return (float)sousTotal / 10;
}

 

float calcMoyenneClasse(int nbEleves, etudiant* classe) {
    float sousTotal = 0;
    for (int i = 0; i < nbEleves; i++) {
        sousTotal = sousTotal + calcMoyenne(classe[i]);
    }
    return sousTotal / (float)nbEleves;
}

 

int  main(int argc, char** argv)
{
    srand((unsigned)time(NULL));
    etudiant robin = createEtudiant();
    //printf("Bonjour mon nom est %s et ma promo est %s\n", robin.nom, robin.promo);
    for (int i = 0; i < 10; i++) {
        //printf("Note %d : %d\n", i, robin.notes[i]);
    }
    //printf("Moyenne : %f\n", calcMoyenne(robin));

 

    etudiant classe[30];
    for (int i = 0; i < 30; i++) {
        classe[i] = createEtudiant();
        printf("Etudiant %d ajoute, avec une moyenne de %f\n", i, calcMoyenne(classe[i]));
    }
    
    float moyenneGenerale = calcMoyenneClasse(30, classe);
    printf("Moyenne generale : %f", moyenneGenerale);
    
    return 0;
}