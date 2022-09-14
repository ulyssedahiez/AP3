#include <stdio.h>

void getAdress(void * variable){

    printf("%p", variable);            

    return;                                                                              
                                                                                                   
}

void getAdressPlusPetite(void * variable1, void * variable2, void * variable3){
    
    printf("pointeurs : %p, %p, %p. \n", variable1, variable2, variable3);

    if (variable1 <= variable2 && variable1 <= variable2){
        printf (" poitneur le plus petit : %p \n",variable1);
    }
    else if(variable2 <= variable3 && variable2 <= variable1){
        printf (" poitneur pointeur le plus petit : %p \n",variable2);
    }
    else if (variable3 <= variable2 && variable3 <= variable1){
        printf (" poitneur le plus petit : %p \n",variable3);
    }
    
    return;
}

void getMeanSum(int* tab, int tailleTab,int * moyenne, int * somme){
    
    
    
    for (int i=0; i<tailleTab; i++){
        *somme += tab[i];
    }
    *moyenne = *somme/tailleTab;
    
    return;

}

void decoupLorem(char * tab){
    
}

int main(){
    
    

    char * lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque tristique risus consequat ipsum sagittis, et hendrerit turpis congue. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aenean bibendum enim eget dolor bibendum, vitae dapibus quam sodales. Suspendisse et nunc eget ipsum efficitur convallis. Curabitur consectetur sapien non urna";



    
    int i[5] = {0,2,4,6,8};
    int moyenne=0;
    int somme=0;
    // appel de la fonction ’getMeanSum’
    getMeanSum(i, sizeof(i)/sizeof(int),&moyenne, &somme);



    printf("La moyenne est %d et la somme est %d \n", moyenne, somme);
    
    
    int a = 12;
    int b = 11;
    int c = 14;
    getAdress(&a);

    getAdressPlusPetite(&a,&b,&c);


}