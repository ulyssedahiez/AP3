#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int estTableauTrie(int* myTableau){
    int count = 0;
    for(int i=0; i < sizeof(myTableau); i++){
        if(myTableau[i]<=myTableau[i+1]){
            count+=1;
        }
    }
    if(count!=sizeof(myTableau)){
        printf("\n le tableau n'est pas trie. \n ");
        return 0;
    }else{
        printf("\n le tableau est trie. \n ");
        return 1;
    }


    return 0;
}

int chiffrementCesar(char* myStr, int key){
    char newStr[50] = "";
    for(int i=0; i < strlen(myStr); i++){
        int lettreEnAscii = (int) myStr[i];
        newStr[i]=lettreEnAscii+key;
    } 
    
    printf(newStr);
    
    return 0;
}

int fusionDeuxTableau(int* tableau1, int* tableau2){



    return 0;
}

int main(){
    int tableau[4] = {1,5,2,8};
    int tableau1[4] = {1,2,3,4};
    int tableau2[4] = {5,6,7,8};
    estTableauTrie(tableau);

    chiffrementCesar("Julien  Mael  Charles  Ulysse", 4);
    
    fusionDeuxTableau(tableau1, tableau2);
    return 0;
}