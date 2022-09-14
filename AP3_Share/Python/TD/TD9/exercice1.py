def exo1():
    n = int(input("Quel est votre nombre ? "))
    carre(n)
    return


def carre(n):
    varDebutFin = ""
    varMiddle = "#"
    for i in range(0, n):
        varDebutFin+="#"
    
    for i in range(0,n-2):
        varMiddle+="$"

    varMiddle+="#"

    print(varDebutFin)
    for i in range(0,n-2):
        print(varMiddle)
    
    if n>1:
        print(varDebutFin)

    return


exo1()