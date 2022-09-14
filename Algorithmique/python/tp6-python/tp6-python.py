# Exercice 1
import math
import TP_3
def obPGCD():
    pgcdpaires = 0
    ib = 0
    jb=0
    for i in range(1,100):
            for j in range(1, 100):
                temppgcd = math.gcd(i, j)
                if(temppgcd>pgcdpaires):
                    pgcdpaires = temppgcd
                    ib = i
                    jb = j
    print("[",ib,"]","[",jb,"] : ",pgcdpaires)

#exo 3

def anneebis():
    tab=[]
    for annee in range(1900, 2021):
        if(len(tab)<30 and TP_3.EstAnneeBis(annee)):
            tab.append(annee)

    mean = sum(tab)/len(tab)
    print(mean)

anneebis()

#exo 2





#obPGCD()
