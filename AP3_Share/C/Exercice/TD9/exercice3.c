#include <stdio.h>
void suite()
{
    FILE *fp1 = fopen("./file_ex3_1.txt", "r");
    FILE *fp2 = fopen("./file_ex3_2.txt", "r");
    FILE *fp_res = fopen("./file_ex3_result.txt", "w");
    int caractereActuel_1 = 0;
    int caractereActuel_2 = 0;
    caractereActuel_1 = fgetc(fp1);
    caractereActuel_2 = fgetc(fp2);
    if (fp1 != NULL)
    {
        while (caractereActuel_1 != EOF)
        {
            printf("%c", caractereActuel_1); // On l'affiche
            fprintf(fp_res, "%c", caractereActuel_1);
            caractereActuel_1 = fgetc(fp1); // On lit le caractère
        }
        fclose(fp1);
    }
    if (fp2 != NULL)
    {
        while (caractereActuel_2 != EOF)
        {
            printf("%c", caractereActuel_2); // On l'affiche
            fprintf(fp_res, "%c", caractereActuel_2);
            caractereActuel_2 = fgetc(fp2); // On lit le caractère
        }
        fclose(fp2);
    }
    fclose(fp_res);
}
void melange()
{
    FILE *fp1 = fopen("./file_ex3_1.txt", "r");
    FILE *fp2 = fopen("./file_ex3_2.txt", "r");
    FILE *fp_res = fopen("./file_ex3_result.txt", "w");
    int caractereActuel_1 = 0;
    int caractereActuel_2 = 0;
    caractereActuel_1 = fgetc(fp1);
    caractereActuel_2 = fgetc(fp2);
    if (fp1 != NULL && fp2 != NULL)
    {
        while (caractereActuel_1 != EOF && caractereActuel_2 != EOF)
        {
            printf("%c", caractereActuel_1);
            fprintf(fp_res, "%c", caractereActuel_1);
            printf("%c", caractereActuel_2);
            fprintf(fp_res, "%c", caractereActuel_2);
            caractereActuel_1 = fgetc(fp1);
            caractereActuel_2 = fgetc(fp2);
        }
        if (fp1 != NULL)
        {
            while (caractereActuel_1 != EOF)
            {
                printf("%c", caractereActuel_1);
                fprintf(fp_res, "%c", caractereActuel_1);
                caractereActuel_1 = fgetc(fp1);
            }
        }
        if (fp2 != NULL)
        {
            while (caractereActuel_2 != EOF)
            {
                printf("%c", caractereActuel_2);
                fprintf(fp_res, "%c", caractereActuel_2);
                caractereActuel_2 = fgetc(fp2);
            }
        }
        fclose(fp1);
        fclose(fp2);
        fclose(fp_res);
    }
}
void main()
{
    int choix;
    while (choix != 1 && choix != 2)
    {
        printf("Faites votre choix\n1. Mélanger les fichiers\n2. Les mettres à la suite\nVotre choix: ");
        scanf("%d", &choix);
    }
    if (choix == 1)
    {
        melange();
    }
    else
    {
        suite();
    }
}

/*
Ecrire une fonction qui fait la fusion de deux fichiers dans un troisième. 
On proposera à l’utilisateur, de manière distincte, de simplement ajouter 
le second fichier à la fin du premier ou d’alterner un caractère pour chaque fichier à tour de rôle 
(comme on mélangerais un paquet de cartes).
A noter : un fichier se termine par le caractère ’EOF’ (End Of File)
*/