#include <stdlib.h>
#include <stdio.h>

 


struct liste_ {
    int value;
    struct liste_* next;
};

typedef struct liste_* liste;

 

struct doubleListe_ {
    int value;
    struct doubleListe_* prev;
    struct doubleListe_* next;
};
typedef struct doubleListe_* doubleListe;

 

liste createNew(int value) {
    liste new = (liste)malloc(sizeof(struct liste_));
    new->value = value;
    new->next = NULL;
    return new;
}

 

void addNew(liste l, int value) {
    if (l == NULL) { l = createNew(value);  return; }
    while (l->next != NULL) {
        l = l->next;
    }
    l->next = createNew(value);
}



doubleListe createNewDouble(int value) {
    doubleListe new = (doubleListe)malloc(sizeof(struct doubleListe_));
    new->value = value;
    new->prev = NULL;
    new->next = NULL;
    return new;
}

 

void addNewDouble(doubleListe l, int value) {
    if (l == NULL) { l = createNewDouble(value);  return; }
    while (l->next != NULL) {
        l = l->next;
    }
    doubleListe newDouble = createNewDouble(value);
    l->next = newDouble;
    newDouble->prev = l;
}

 

int  main()
{
    liste new = createNew(0);
    for (int i = 1; i < 10; i++) {
        addNew(new, i);
    }

 

    liste temp = new;
    int nombreElements = 0;

 

    while (temp != NULL) {
        nombreElements++;
        printf("%d ", temp->value);
        temp = temp->next;
    }

 

    printf("\nNombre final d'elements dans la chaine : %d\n", nombreElements);
}