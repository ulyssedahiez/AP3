
def InferieurA(a, tableau):
    retour = []
    for flottant in tableau:
        if(flottant < a):
            retour.append(flottant)
        pass
    return retour

def SommetMoyenne(tableau):
    moyenne = 0
    somme = 0

    for chiffre in tableau:
        somme = somme + chiffre
        pass
    moyenne = somme / len(tableau)
    return (somme, moyenne)

def TabPair(tableau):
    pair = []

    for entier in tableau:
        if(entier%2 == 0):
            pair.append(entier)
        
    return pair

def Tronque(tableau):
    retour = []
    for flottant in tableau:
        retour.append(int(flottant))
        pass
    return retour

exemple = [43, 3.2, 4.43, 2, 14, 9]

print(InferieurA(10 ,exemple))
print(SommetMoyenne(exemple))
print(TabPair(exemple))
print(Tronque(exemple))
