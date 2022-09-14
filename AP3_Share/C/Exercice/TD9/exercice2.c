#include <stdio.h>

int main(){

    FILE * fp=fopen("./ficExercice2.txt", "r");
    int caractereActuel = 0;
    
    if(fp != NULL){
        while (caractereActuel != EOF){
            caractereActuel = fgetc(fp); // On lit le caractère
            printf("%c", caractereActuel);
        }
        fclose(fp);
    }
    return 0;
}


//En utilisant fgetc, lire caractère par caractère un fichier contenant plu- sieurs lignes de texte et 
//l’afficher ligne par ligne. (par exemple en détectant la présence de \n lors de la lecture)