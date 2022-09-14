#include <stdio.h>

int main()
{
    FILE * fp=fopen("./ficExercice1.txt", "w");

    int nbPremier [10] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};

    int longueur = sizeof(nbPremier)/sizeof(nbPremier[0]);

    for(int i = 0; i < longueur; i++){
        fprintf(fp, "%d ", nbPremier[i]);
    }
 
    fclose(fp);
    return 0;
}

//Développer une fonction qui prends un datastream
//et y range les n pre- miers nombres premiers.
