
#On suppose qu’une ann ́ee y est bissextile si et 
#eulement si elle est multiple de 4 mais pas de 100, ou bien multiple de 400. 
#Proposez une fonction qui d ́etermine si une ann ́ee est bissextile ou non.

a = int(input("Entrez l'année : "))

def isBissextile (a) :
    if(a % 4 == 0 and a % 100 != 0) :
        print "L'année est bissextile"
    elif(a % 4 == 0 and a % 100 == 0 and a % 400 == 0) :
        print "L'année est bissextile"
    else:
        print "L'année n'est pas bissextile"

isBissextile(a)