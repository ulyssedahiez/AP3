from random import randint

"""
Le code ADN peut ˆetre repr ́esent ́e avec les lettres A T G C
3. En supposant une chaˆıne de caract`eres donn ́ee en entr ́ee,  ́ecrire une fonction qui recherche
 dans le code al ́eatoire la pr ́esence ou non de cette chaˆıne de caract`eres.
4. Ecrireunefonctionquirenvoielepourcentagedechaˆınededeuxlettres (”ag”, ”tc”...)
"""



def adn():
    chaine = ["A", "T", "G", "C"]
    adn = []

    for i in range(0,500):
        while True :
            rang = randint(0,3)
            if i == 0 :
                adn+=[chaine[rang]]
                break

            if i > 0 :
                if adn[i-1] != chaine[rang] :
                    adn+=[chaine[rang]]
                    break
    return adn


def pourcentage():
    chaine = adn()
    a=0
    t=0
    g=0
    c=0
    for i in range(0,len(chaine)):
        if chaine[i]=="A":
            a+=1
        if chaine[i]=="T":
            t+=1
        if chaine[i]=="G":
            g+=1
        if chaine[i]=="C":
            c+=1
    
    total = a + t + g + c
    print("Le pourcentage de A est de "+str(100*a/total)+"%")
    print("Le pourcentage de T est de "+str(100*t/total)+"%")
    print("Le pourcentage de G est de "+str(100*g/total)+"%")
    print("Le pourcentage de C est de "+str(100*c/total)+"%")
    return

pourcentage()
