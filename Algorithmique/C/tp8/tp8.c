#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

void diviseri(int a){
    printf("%i",a);
}
void diviserf(double a){
    
    printf("%f", a);
    
}

void afficher(int a, int b){
float c= (float) a/b;
    
    void (*ptr)();
    if(c !=(int)c){
        (ptr)=&diviserf;
    }else{
         (ptr)=&diviseri;
    }
    ptr(c);
}

void sumNumbers(int argNum, ...) {
    // argNum est le nombre d'argument !!!
    va_list ap;
    va_start (ap, argNum);
    int somme = 0;
    while (argNum > 0) {
        int n = va_arg(ap, int);
        somme += n;
        printf("Argument index : %d, Argument value %d, Sum : %d\n", argNum, n, somme);
        argNum--;
    }
    va_end(ap);
    printf("Somme totale = %d\n", somme);
}

void carre(int argNum, ...){
    while (argNum > 0) {
        
        argNum--;
    }
}

int main(){


    sumNumbers(3, 5, 74, 78);
    afficher(10,12);
    



    return 0;
}