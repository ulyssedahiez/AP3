import math

""" Exercice 1 """
def ex1():
    ajoutsDansListe([])
    return

def ajoutsDansListe(liste):
    nouvelleValeur = int(input("Valeur à ajouter : "))
    if(nouvelleValeur > 0):
        liste = liste + [nouvelleValeur]
        ajoutsDansListe(liste)
    else:
        print(liste)
    return liste

""" Exercice 2 """
def valeurScrabble(motArgument):
    mot = motArgument.lower()
    if mot[0]=="a" or mot[0]=="e" or mot[0]=="i" or mot[0]=="o" or mot[0]=="u" or mot[0]=="n" or mot[0]=="r" or mot[0]=="t" or mot[0]=="l" or mot[0]=="s":
        valeur = 1
    elif mot[0]=="d" or mot[0]=="g":
        valeur = 2
    elif mot[0]=="b" or mot[0]=="c" or mot[0]=="m" or mot[0]=="p":
        valeur = 3
    elif mot[0]=="f" or mot[0]=="h" or mot[0]=="v" or mot[0]=="w" or mot[0]=="y":
        valeur = 4
    elif mot[0]=="k":
        valeur = 5
    elif mot[0]=="j" or mot[0]=="x":
        valeur = 8
    elif mot[0]=="q" or mot[0]=="z":
        valeur = 10
    else:
        valeur = 0
    if len(motArgument)>=2:
        valeur = valeur + valeurScrabble(motArgument[1:])
        return valeur
    else:
        return valeur

def ex2():
    phrase="Ceci est une phrase de test complexe".split()
    phraseTri = sorted(phrase, key=valeurScrabble)
    print(phraseTri)
    return

"""Exercice 3"""
def ex3():
    exemple=[0,3,1.5,8,-10]
    print("Tableau : ",exemple)
    print("Tableau <5 : ",parcoursRecursif(exemple,5,0,[]))
    print("Somme : ",sommeRecursif(exemple,0))
    print("Moyenne : ",moyenneRecursif(exemple))
    print("Troncature : ", tronqueRecursif(exemple,0))
    print("Nombres pairs : ",pairsRecursif(tronqueRecursif(exemple,0),0,[]))
    return
    
def parcoursRecursif(table, a, indice, resultat):
    if indice==len(table):
        return resultat
    elif table[indice]<a:
        resultat = parcoursRecursif(table, a, indice+1, resultat+[table[indice]])
        return resultat
    else:
        resultat = parcoursRecursif(table, a, indice+1, resultat)
        return resultat

def sommeRecursif(table, indice):
    if indice==len(table):
        return 0
    else:
        return table[indice]+sommeRecursif(table, indice+1)

def moyenneRecursif(table):
    return sommeRecursif(table,0)/len(table)

def tronqueRecursif(table, indice):
    if indice==len(table):
        return table
    else:
        table[indice]=math.floor(table[indice])
        return tronqueRecursif(table, indice+1)

def pairsRecursif(table, indice, resultat):
    if indice==len(table):
        return resultat
    elif (table[indice]%2==0):
        resultat = pairsRecursif(table, indice+1, resultat+[table[indice]])
        return resultat
    else:
        resultat = pairsRecursif(table, indice+1, resultat)
        return resultat

""" Exercice 4 """
def ex4():
    exemple=[0,3,1.5,8,-10]
    triBulleRecursif(exemple, 0)
    return

def triBulleRecursif(table, indice):
    print("---")
    print(indice)
    print(table)
    # on gère le cas du bout de la liste pour ne pas faire de dépassement
    if indice+1==len(table)-1 and table[indice]<=table[indice+1]:
        print("tri fini")
        return table
    elif indice+1==len(table) and table[indice]>table[indice+1]:
        temp = table[indice+1]
        table[indice+1] = table[indice]
        table[indice] = temp
        return triBulleRecursif(table, 0)
    # cas normal
    elif table[indice]<table[indice+1]:
        return triBulleRecursif (table, indice +1)
    else:
        print("changement entre ",indice," et ",indice+1)
        temp = table[indice+1]
        table[indice+1] = table[indice]
        table[indice] = temp
        return triBulleRecursif(table, 0)


""" Exercice 5 """
def ex5():
    exemple = saisieUtilisateur([])
    #exemple = [(1,3), (-1,1), (4, 7), (10, 12)]
    print(exemple)
    if len(exemple)<2:
        print("pas assez de points..")
        return
    #on prends les coordonnées des deux premiers points
    xA = exemple[0][0]
    yA = exemple[0][1]
    xB = exemple[1][0]
    yB = exemple[1][1]
    #on trouve la droite qui passe par ces deux points, sous la forme ax+b
    if(yA == yB):
        #(cas particulier de droite verticale)
        a = 0
        b = yA
    else :
        a = (xB-xA)/(yB - yA)
        b = yA - a*xA			
    resultat = checkDroite(exemple, a, b, 2)
    print ("Tous les points passent par une seule droite : ", resultat)
    return resultat

def checkDroite(table, a, b, indice):
    if indice==len(table):
        return True
    else:
        xTest = table[indice][0]
        yTest = table[indice][1]
        validation = (a*xTest+b==yTest)
        return validation and checkDroite(table, a, b, indice+1)

""" Saisie des points par l'utilisateur """
def saisieUtilisateur(table):
    continuer = str(input("Continuer? y/n :"))
    if continuer == "y":
        x = int(input("x ?"))
        y = int(input("y ?"))
        table=saisieUtilisateur(table + [(x,y)])
    return table

if  __name__=="__main__":
	#ex1()
	#ex2()
	#ex3()
	#ex4()
	ex5()