#include <stdio.h>
#include <stdlib.h>

int multiplication(int a, int b){
    return a*b;
}



int main()
{
    int entierA;
    int entierB;

    printf("Quel est ton premier nombre ? ");
    scanf("%d", &entierA);
    printf("Quel est ton second nombre ? ");
    scanf("%d", &entierB);

    
    printf("\n Ton nombre est %d", multiplication(entierA, entierB));

    return 0;
}
