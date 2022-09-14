#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct chat{
    char * nom[10];
    char * couleur[6];
};

int main()
{
    struct chat chat1;
    printf("Quel est le nom de votre chat ? ");
    scanf("%s", *chat1.nom);
    
    printf("%s\n", chat1.nom);

    return 0;
}
