#include <stdio.h>



int doubler(int a){return a*2;}

int tripler(int a){return a*3;}

int quintupler(int a){return a*4;}

int plusDeux(int a){return a+2;}

int moinsDeux(int a){return a-2;}

int miseAZero(int a){return 0;}


void calcul(char * str,int a){
    if(str == "doubler"){
        printf("tu es bien dans la partie doubler");
    }else{
        printf("tu t'es trompé de paramète");
    }
}


int main(){
    calcul("doubler",2);
    return 0;
}