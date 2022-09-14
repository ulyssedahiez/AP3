#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int multiplier(int a){
    a= a*10;
    return a;
    printf("a\n", a);
}
int diviser(int a){
    a= a/10;
    return a;
    printf("a\n", a);
}

int appelerFonction(int nombre){
    int (*pfd)(int);
    if(nombre%10 == 0){
        pfd = &diviser; 
    }else{
        pfd = &multiplier;
    }
    int res = (*pfd)(nombre);

    printf("res : %i", res);
    return res;
}

int main(){

    appelerFonction(13);
    return 0;
}







