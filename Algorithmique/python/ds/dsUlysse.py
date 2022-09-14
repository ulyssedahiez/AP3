#Exercice 1

def fonctliste(liste):

    if len(liste) == 1:
        return liste[0]

    elif len(liste) >= 2 and liste[0] != liste[len(liste)-1]:
        return liste[0], liste[len(liste)-1]

    elif liste[0] == liste[len(liste)-1] and liste[0] != liste[len(liste)-2]:
        return liste[0], liste[len(liste)-1]

    elif liste[0] == liste[len(liste    :mge
    1] and liste[0] == liste[len(liste)-1]:
        return liste[0], liste[len(liste)-2]
    else:
        for i in range(0, len(liste)-2):
            count = 0
            if (liste[i]==liste[i+1]):
                count+=1
        if count == len(liste):
            return liste[0]
"""
print(fonctliste([0]))   
print(fonctliste([0,1,2,3,4])) 
print(fonctliste([0,1,2,3,0])) 
print(fonctliste([0,0,0,0,0])) """

#Exercice 2

def date(jour, mois, annee):

    if jour>0 and jour < 31 and mois>0 and mois<13:
        return [jour, mois, annee]
    else:
        return "date mauvaise"


def jours(jours, jours2):
    nbj=0
    j = 0
    a=0
    m=0

    j= jours[0]-jours2[0]
    
    m = jours[1] - jours2[1]
    mm = m*30
    a = jours[2] - jours2[2]
    aa= a*365

    nombre = j+mm+aa
    if nombre >=0:
        return nombre
    else:
        return abs(nombre)

# print(jours([1,2,2021], [30,4,2021]))

    
# exo 3



# exo 4

def conway(num):
    T = [[0] * (num+1) for p in range(num+1)] 
    for num in range(num+1): #pour toute les iterations de n on fait la suite
        if num == 0:
            T[num][0] = 1 # si c'est le premier on le remet à un
        else:
            for k in range(num+1): #on calcule pour toute la ligne (plus un car c'est un triangle)
                if k == 0:
                    T[num][0] = 1 #on multiplis pour le premier cas
                else:
                    T[num][k] = T[num-1][k-1] + T[num-1][k]  #on prend les deux valeurs du dessu

    for i in range(0,len(T)-1):
        print(T[i])


#conway(8)

# exo 5

def estsous(suite, soussuite):
    if soussuite in suite:
        return True

def toutesous():




    




