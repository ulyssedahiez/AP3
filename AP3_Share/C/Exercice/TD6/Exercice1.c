main () {
int A = 1; 
int B = 2;
int C = 3; 
int *P1, *P2;
P1=&A; //
P2=&C; // L'@ de variable du pointeur P2 est l'adresse de C
*P1=(*P2)++; //P1 est égale à 4
P1=P2; // L'@ de variable du pointeur P1 est maintenant le même que celui de P2
P2=&B; // L'@ de variable du pointeur P2 est l'@ de B
*P1-=*P2; //P1 = 0
++*P2; // P2 = 1
*P1*=*P2; 
A=++*P2**P1; 
P1=&A; //L'@ de variable du pointeur P1 est l'@ de A
*P2=*P1/=*P2; 
return 0;
}


//Donner pour chaque ligne les valeurs de A, B, C, P1 et P2 qui ont changé
