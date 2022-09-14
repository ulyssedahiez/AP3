#include <stdio.h>


void main(){
    char* elem[9] = {"Daniel", "Brandon", "Oliver", "Johnny", "Sylvie", "Moha", "Rodolphe", "Sophie", "Henri"} ;
    for(int i= 0; i<sizeof(elem); i ++){
        printf("dans la classe il y a %s\n", elem[i]);
    }



}