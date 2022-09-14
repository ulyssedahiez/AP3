/**
 * @file DAHIEZ_Ulysse_CC_AP3_C_2022.c
 * 
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2022-02-11
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
question de cours :
1) 
char : 1 octets
int : 4 octets
long : 4 octets
double : 8 octets
long double : 12 octets
2)
for (int i=0; i<10; i++){
    printf("%i",i);
}

3)
int a =2;
int * ptrint = &a;

void * ptrgen = NULL;
int a = 2;
ptrgen = &a;

int ptr

int * char tab = {"e","b","c"};
char b = tab[2];



4)
Calloc alloue un bloc de mémoire en initialisant tous ces octets à la valeur 0.

*/

// ----------exo 1-----------

void carre(int n){
    for (int i=0;i<=n;i++){
        printf("*");
    for (int j=0;j<=n;j++){
    if ((i==0) || (i==n)){
        printf("*");
    }else{
        printf(" ");
    }
    }
    printf("*\n");
    }
}

// ----------exo 2-----------

void triTrois(int* val1, int*val2, int*val3){
    int* temp;
printf("val1 : %i  val2 : %i val3 : %i ", *val1, *val2, *val3);


    if (*val1>*val2) {
        *temp = *val1;
        *val1 = *val2;
        *val2 = *temp;
        }
    if (*val1>*val3){
        *temp = *val1;
        *val1 = *val3;
        *val3 = *temp;
        }
    if (*val2>*val3){
        *temp = *val2;
        *val2 = *val3;
        *val3 = *temp;
        }

 printf("\n \n val1 : %i  val2 : %i val3 : %i ", *val1, *val2, *val3);
  
}

// ----------exo 3-----------

char  inttochar(int n){
    char text[20]; 
    return sprintf(text, "%d", n);
}

// ----------exo 4-----------
struct Athlete_{
    char* nom;
    char categorie;
    int score;
};
typedef  struct  Athlete_ * athlete;

athlete  createNewDouble(char* mynom, char mycategorie, int myscore) {
    athlete  atl = malloc(sizeof(struct Athlete_));
    atl -> nom = mynom;
    atl ->categorie;
    atl ->score;
    
    return  atl;
}

// ----------exo 5-----------

struct Liste_{
    int val;
    struct Liste_ * next;
};
typedef  struct  Liste_ * liste;

liste  createNew(int v) {
    liste  elt = malloc(sizeof(struct Liste_));
    elt -> val = v;
    elt ->next = NULL;

    return  elt;
}

void  add(liste l, int  new) {
    if(l==NULL) { 
        l=createNew(new);
        return;
    }
    while(l->next!=NULL) {
        l=l->next;
    }

        l->next=createNew(new);

}

void showListe(liste val){
    int counter = 0;
    while (val != NULL){
        printf(" %i,",val->val);
        val = val->next;
        counter +=1;
    }
}

void changer(liste L1, int occu1, int occu2){
    liste L1Next = L1;
    liste L1Prev = L1;
    liste L2Next = L1;
    liste L2Prev = L1;
    liste L2 = L1;
    for(int i=1; i<occu1; i++){
        L1 = L1->next;
    }
    for(int i=1; i<occu1-1; i++){
        L1Prev = L1Prev->next;
    }
    for(int i=1; i<occu1+1; i++){
        L1Next = L1Next->next;
    }

    for(int i=1; i<occu2; i++){
        L2 = L2->next;
    }
    for(int i=1; i<occu2-1; i++){
        L2Prev = L2Prev->next;
    }
    for(int i=1; i<occu2+1; i++){
        L2Next = L2Next->next;
    }

    L2Prev->next = L1;
    L1Prev->next = L2;
    L1->next = L2Next;
    L2->next = L1Next;
    
}

void trier(liste l){
    liste iter = l;
    while (iter->next != NULL){
        while (iter->next != NULL){
    }
}



int main(){
    //carre(10);
    int a = 5;
    int b = 1;
    int c = 3;

    //triTrois(&a, &b, &c);


    liste l = createNew(1);
    add(l,5);
    add(l,3);
    add(l,12);
    add(l,8);
    add(l,0);
    add(l,7);

    showListe(l);
    
    changer(l, 2,4);
    showListe(l);

    return 0;
}