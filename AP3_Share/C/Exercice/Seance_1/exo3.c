#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h> 
#include <string.h>

int bisextille (int annee)
{ 
    int res = 1;
    if ((annee % 400 == 0) || ((annee % 100 != 0) && (annee % 4 == 0)))
        res = 1;
    else
        res = 0;
    return res;
}



int main()
{
    char * date;
    char * dateSplit;


    printf("Quelle est ta date ? ");
    scanf("%s",date);
    printf("\n %s", date);

    dateSplit=strtok(date, "/");

    printf("\n %s", dateSplit);
    
    dateSplit=strtok(dateSplit "/");

    printf("\n %s", dateSplit);


    return 0;
}
