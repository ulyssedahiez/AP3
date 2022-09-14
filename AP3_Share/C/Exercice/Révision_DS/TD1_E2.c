/* 
Proposer un programme qui prends deux nombres entiers saisis par l’utilisateur et affiche leur produit.
*/
#include <stdio.h>


int produit(int a, int b){
    return a*b;
}


int main(){
    int nombreA;
    int nombreB;

    printf("%s","Saisir votre premier nombre : ");
    scanf("%d",&nombreA);

    printf("%s","Saisir votre deuxième nombre : ");
    scanf("%d",&nombreB);

    int result = produit(nombreA, nombreB);

    printf("%dx%d=%d", nombreA, nombreB, result);
    return 0;
}