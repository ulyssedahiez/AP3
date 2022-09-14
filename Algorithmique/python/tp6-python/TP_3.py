import math

# Exercice 1

def EstPaire( nombre):
    if(nombre%2 == 0):
        print(nombre, " est un nombre paire.")
    if(nombre%2 != 0):
        print(nombre, " est un nombre impaire.")

# EstPaire(2)
# EstPaire(3)
# EstPaire(2.8)

# Exercice 2

def EstAnneeBis(annee):
    if(( annee%4 == 0 and annee%100 != 0 ) or annee%400 == 0):
        return True
    else:
        return  False
    

    
# EstAnneeBis(2018)
# EstAnneeBis(2020)

# Exercice 3

def Polynome(a, b ,c):
    delta = (b*b)-(4*a*c)

    if(delta == 0):
        xun = (-b)/2*a
        print("delta = 0, le polynome n'a qu'une solution : x = ", xun)

    if(delta < 0):
        print("pas de solution possible")

    else:
        delta = (b*b)-(4*a*c)
        xun = (-b-math.sqrt(delta))/2*a
        xdeux = (-b+math.sqrt(delta))/2*a

        print("le polynome admet deux solution tel que x1 = ", xun, "et x2 = ", xdeux)

    

# Polynome(-3, 7, 1)

# Exercice 4

def Factoriel(entier):
    if (entier > 1):
        entier *= Factoriel(entier-1)
    return entier

# print (Factoriel(5))

# Exercice 5

def entToBinHex(entier):
    print("nombre en decimal : ", entier)
    nombin = ""
    nomhex = ""
    entierb = entier
    entierh = entier

    while entierb!= 0:
        if entierb%2 == 0:
            nombin = nombin +"0"
        else:
            nombin = nombin +"1"
        entierb = entierb//2
    print("nombre en binaire  : ", "".join(reversed(nombin)))

    while entierh != 0:

        if (entierh%16 >= 0 and entierh%16 < 10):
            nomhex = nomhex + str(entierh%16)
        if (entierh%16 == 10):
            nomhex = nomhex + "A"
        if (entierh%16 == 11):
            nomhex = nomhex + "B"
        if (entierh%16 == 12):
            nomhex = nomhex + "C"
        if (entierh%16 == 13):
            nomhex = nomhex + "D"
        if (entierh%16 == 14):
            nomhex = nomhex + "E"
        if (entierh%16 == 15):
            nomhex = nomhex + "F"

        entierh = entierh//16

    print("nombre en hexadecimal :", nomhex)


# entToBinHex(456)


# Exercice 6

def Syracuse(entier):
    tab = []
    for i in range(0, entier):
        if (entier%2 == 0):
            entier = entier/2
        else:
            entier = (3*entier)+1

        tab.append(entier)
    print(tab)


#Syracuse(100)


# Exercice 7

def flotant(Float1):
    signe = ""
    nombin = ""
    nombindec = ""
    

    if Float1 >= 0:
        signe = "0"
        
    else:
        signe = "1"
        Float1 = -Float1
    
    pent =  math.floor(Float1)
    
    pdec = Float1-pent
    print("pent : ",pent, " , pdec : ", pdec)

    while pent!= 0:
        if pent%2 == 0:
            nombin = nombin +"0"
        else:
            nombin = nombin +"1"
        pent = pent//2
    print("pdec :: ",pdec)
    while pdec!= 0:
        
        if (pdec*2 < 1.0 ):
            nombindec = nombindec +"0"
            pdec *= 2
            
        elif pdec*2 >= 1.0:
            nombindec = nombindec +"1"
            pdec *= 2
            pdec-=1
            
        elif pdec*2 == 1:
            nombindec = nombindec +"1"
            pdec-=1

    fonc = nombin[1:7] + nombindec

    zero =""
    for i in range(0, 17- len(fonc)):
        zero= zero +"0"
    fonc = fonc + zero

    Exposent = (127)+len(nombin)-1
    print("Exposent", Exposent)
    expbin = ""
    while Exposent!= 0:
        if Exposent%2 == 0:
            expbin = expbin +"0"
        else:
            expbin = expbin +"1"
        Exposent = Exposent//2

    expbin = "".join(reversed(expbin))

    print("(",signe,")(",expbin,")(",fonc,")")
    
# 0.0011
#flotant(-85.1875)