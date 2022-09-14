#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


// test si l'année est bissextile
bool bisextile(int annee_entree){
    if(annee_entree%4 == 0){
        if(annee_entree%4 == 0){
            return true;
        }
        else{
            return false;
        }
    }
    else{
        return false;
    }
}

//test le nombre de jours dans le mois
int joursdanslemois(int mois_entree, int annee){
    bool estbissextile;
    if (mois_entree == 02){
        estbissextile = bisextile(annee);
        if(estbissextile == true){
            return 29;
        }else{
            return 28;
        }
    }
    //pour les mois inférieurs à juillet
    else if(mois_entree <= 7){
        if(mois_entree%2 == 0){
            return 30;
        }
        else{
            return 31;
        }
        
    }
    else{
        if(mois_entree%2 == 0){
            return 31;
        }
        else{
            return 30;
        }
    }
}

// test si l'entree de l'utilisateur est valide
void valide(int jour, int mois, int annee, int jours_sup){
    int jours_max = joursdanslemois(mois, annee);
    if(jour <= 0 || jour > jours_max || mois <= 0 || mois > 12 || jours_sup < 0){
        printf("\nles données en entrée ne sont pas valides\n");
        printf("fin du programme\n");
        exit(0);
    }
    else{
        printf("\nl'entrée est valide\n");
    }
}



int main() {
    //Variables
    int jour, mois, annee, jours_sup;
    int jours_max, jours_reste, valinter, jours_sup_origin;

    //programme
    printf("Entrez une date jj/mm/AAAA: ");
    scanf("%d/%d/%d",&jour, &mois, &annee);
    printf("Donnez un nombre de jour(s) a ajouter: ");
    scanf("%d", &jours_sup);
    printf("\nVos valeurs en entrée:\n");
    printf("jour: %d\n", jour);
    printf("mois: %d\n", mois);
    printf("annee: %d\n", annee);
    printf("jour supplémentaires: %d\n", jours_sup);
    jours_sup_origin = jours_sup;
    // 1 ere étape test de validité
    valide(jour, mois, annee, jours_sup);

    //récupération du jour max dans le moi
    while(jours_sup != 0){
        jours_max = joursdanslemois(mois, annee);
        jours_reste = jours_max - jour; //jours restant pour la fin du mois
        //printf("jours restants dans le mois en cours: %d\n",jours_reste);
        if (jours_reste >= jours_sup){ //cas où uniquement les jours sont a incrémenter
            valinter = jour + jours_sup;
            jour = valinter;
            jours_sup = 0; 
        }
        else{
            valinter = jours_sup - jours_reste;
            jours_sup = valinter;
            if( mois != 12){
                mois++;
            }
            else{
                mois = 01;
                annee++;
            }

            jours_sup--;
            jour = 01;
        }

    }

    printf("\ndate finale dans %d jours:\n", jours_sup_origin);
    printf("jour: %d\n", jour);
    printf("mois: %d\n", mois);
    printf("annee: %d\n", annee);
}

