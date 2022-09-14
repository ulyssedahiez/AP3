#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Liste_{
    int val;
    struct Liste_ * next;
};
typedef  struct  Liste_ * liste;

struct ListeD_{
    int val;
    struct ListeD_ * prev;
    struct ListeD_ * next;
};
typedef  struct  ListeD_ * listeD;


listeD  createNewDouble(int v) {
    listeD  elt = malloc(sizeof(struct ListeD_));
    elt -> val = v;
    elt ->prev = NULL;
    elt ->next = NULL;
    
    return  elt;
}

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

void  addDouble(listeD l, int  new) {
    if(l==NULL) { 
        l=createNewDouble(new);
        return;
    }
    while(l->next!=NULL) {
        l=l->next;

    }
        l->next=createNewDouble(new);
        l->next->prev = l;
}

void countElemList(liste val){
    int counter = 0;
    while (val != NULL){
        printf(" %i,",val->val);
        val = val->next;
        counter +=1;
    }
    printf("\n\nil y a %i elements.\n", counter);
}

void countElemDoubleList(listeD val){
     int counter = 0;
    while (val != NULL){
        printf(" %i,",val->val);
        val = val->next;
        counter +=1;
    }
    printf("\n\nil y a %i elements.\n", counter);

}

void fusionListe(liste L1, liste L2){
    while (L1->next != NULL){
        L1 = L1->next;
    }
    L1->next = L2; 
}
void fusionListeDouble(listeD L1, listeD L2){
    while (L1->next != NULL){
        L1 = L1->next;
    }
    L1->next = L2;
}

void addmiddleElem(liste L1, liste new,int occu){
    liste L1Next = L1;
    for(int i=1; i<occu; i++){
        L1 = L1->next;
    }
    for(int i=1; i<occu+1; i++){
        L1Next = L1Next->next;
    }
    
    L1->next = new;
    new->next = L1Next;

}
void addmiddleElemDouble(listeD L1, listeD new,int occu){
    listeD L1Next = L1;
    for(int i=1; i<occu; i++){
        L1 = L1->next;
    }
    for(int i=1; i<occu+1; i++){
        L1Next = L1Next->next;
    }
    
    L1->next = new;
    new->next = L1Next;
    new->prev = L1;
    L1Next->prev = new;

}

void supprElem(liste L1, int occu){
    liste L1Next = L1;
    liste L1Prev = L1;
    for(int i=1; i<occu; i++){
        L1 = L1->next;
    }
    for(int i=1; i<occu-1; i++){
        L1Prev = L1Prev->next;
    }
    for(int i=1; i<occu+1; i++){
        L1Next = L1Next->next;
    }
    L1Prev->next = L1Next;
    free(L1);
}

void supprElemDouble(listeD L1, int occu){
    listeD L1Next = L1;
    listeD L1Prev = L1;
    for(int i=1; i<occu; i++){
        L1 = L1->next;
    }
    for(int i=1; i<occu-1; i++){
        L1Prev = L1Prev->next;
    }
    for(int i=1; i<occu+1; i++){
        L1Next = L1Next->next;
    }
    L1Prev->next = L1Next;
    L1Next->prev = L1Prev;
    free(L1);
}
      
int main(){
    liste l = createNew(1);
    add(l,42);
    add(l,35);
    add(l,28);
    //countElemList(l);

    listeD ld = createNewDouble(1);
    addDouble(ld, 40);
    addDouble(ld,56);
    addDouble(ld,84);
    addDouble(ld,64);
    //countElemDoubleList(ld);

    liste l2 = createNew(1);
    add(l2,78);
    add(l2,67);
    add(l2,468);
    add(l2,8);
    add(l2,78);
    fusionListe(l,l2);
    countElemList(l);

    liste test = createNew(4);
    addmiddleElem(l2, test, 2);
    countElemList(l2);
    supprElem(l2,3);

    countElemList(l2);

    return 0;
}

