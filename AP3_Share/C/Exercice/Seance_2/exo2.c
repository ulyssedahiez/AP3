#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    int cle;
    char * chaine;
    char * code;

    char lettre[52]= "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"; 

    printf("Quelle est votre chaine de caractère ? ");
    scanf("%s", chaine);

    printf("Quelle est votre clef ? ");
    scanf("%d", &cle);
    printf("\n");
    //printf("Votre chaine codée est : ");

    for(int i =0;i<strlen(chaine);++i){
        int a = 0;
        for(int b = 0; b<strlen(lettre);++b){
            if(&chaine[i]==&lettre[b]){
                a = b;
            }
            printf("%d", a);
        }
        printf("%s", &lettre[a]);
    }


    

    return 0;
}