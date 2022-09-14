#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void Tri(int *liste, int longueur)
{
    int compteur = 0;
    int swap = 0;
    for (int i = 0; i < (longueur - 1); i++)
    {
        if (liste[i] > liste[i + 1])
        {
            swap = liste[i];
            liste[i] = liste[i + 1];
            liste[i + 1] = swap;
            compteur++;
        }
        if (compteur != 0)
        {
            Tri(liste, longueur);
        }
    }
}
char *concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

void main()
{
    FILE *fp = fopen("./file_ex4_origin.txt", "r");
    int nb_element = 0;
    char caractereActuel = 0;
    if (fp != NULL)
    {
        caractereActuel = fgetc(fp);
        while (caractereActuel != EOF)
        {
            caractereActuel = fgetc(fp);
            if (caractereActuel == '\n')
            {
                nb_element++;
            }
        }
    }
    fclose(fp);
    printf("%d \n\n\n", nb_element);
    fp = fopen("./file_ex4_origin.txt", "r");
    int liste[nb_element];
    int compteur = 0;
    char *temp;
    if (fp != NULL)
    {
        caractereActuel = fgetc(fp);
        while (caractereActuel != EOF)
        {
            if (caractereActuel != '\n')
            {
                temp = concat(temp, caractereActuel);
                caractereActuel = fgetc(fp); // On lit le caractère
            }
            else
            {
                liste[compteur] = atoi(temp);
                printf("%d", liste[compteur]);
                compteur++;
            }
        }
    }
    fclose(fp);
    //int liste []= {45,12,5,26,32,87,1,2,6,24,63};
    int longueur = sizeof(liste) / sizeof(liste[0]);
    //Tri(liste, longueur);
    for (int i = 0; i < longueur; i++)
    {
        printf("%d\n", liste[i]);
    }
}