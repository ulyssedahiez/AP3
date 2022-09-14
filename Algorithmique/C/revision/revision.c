#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct matrice{
    int Aa;
    int Ab;
    int Ac;
    int Ba;
    int Bb;
    int Bc;
    int Ca;
    int Cb;
    int Cc;
};
typedef struct matrice * matriceP;

void newValue(int* a, int newEntier){
    *a = newEntier;
}

int main(){

    int a = 5;
    printf("-> %i \n",a);
    newValue(&a,10);
    printf("-> %i \n",a);


    matriceP 



}