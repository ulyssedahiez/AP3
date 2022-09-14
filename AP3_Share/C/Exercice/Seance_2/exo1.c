#include <stdio.h>
#include <stdlib.h>

int main()
{
    /*
    //PARTIE 1
    int a = 5;
    int b = 10;
    int * ptrX = &a;
    int * ptrY = &b;
    b++; //b->11
    a++; //a->6
    *ptrX = a+b; //a->17
    *ptrY = b+*ptrX; //b->28
    (*ptrY)++; //a->18
    (*ptrX)++; //b->29
    printf("%d\n",*ptrX);
    printf("%d\n",*ptrY);
    return 0;
    */

    //PARTIE 2
    int a = 5;
    int b = 10;
    int * ptrX = &a;
    int * ptrY = &b;
    b++; //b->11
    a++; //a->6
    *ptrX = a+b; //a->17
    *ptrY = b+*ptrX; //b->28
    ptrX = ptrY; //a->28
    (*ptrX)++; //a&b->29 car ptrX=ptrY
    printf("%d\n",*ptrX);
    printf("%d\n",*ptrY);
    return 0;

}



