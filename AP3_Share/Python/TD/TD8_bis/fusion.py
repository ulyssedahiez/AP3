import random
from datetime import datetime,timedelta
#Nombre aléatoire n
def aleatoire(n):
    tableau=[]
    for i in range(0,102):
        tableau+=[random.randint(0,n)]
    return tableau


#Tri fusion fonction de division du tableau
def tri_fusion(tableau):
    if  len(tableau) <= 1: 
        return tableau
    pivot = len(tableau)//2
    tableau1 = tableau[:pivot]
    tableau2 = tableau[pivot:]
    gauche = tri_fusion(tableau1)
    droite = tri_fusion(tableau2)
    fusionne = fusion(gauche,droite)
    return fusionne



#Tri fusion fonction de fusion de 2 listes
def fusion(tableau1,tableau2):
    global compteur
    indice_tableau1 = 0
    indice_tableau2 = 0    
    taille_tableau1 = len(tableau1)
    taille_tableau2 = len(tableau2)
    tableau_fusionne = []
    while indice_tableau1<taille_tableau1 and indice_tableau2<taille_tableau2:
        if tableau1[indice_tableau1] < tableau2[indice_tableau2]:
            tableau_fusionne.append(tableau1[indice_tableau1])
            indice_tableau1 += 1
        else:
            tableau_fusionne.append(tableau2[indice_tableau2])
            indice_tableau2 += 1
    while indice_tableau1<taille_tableau1:
        tableau_fusionne.append(tableau1[indice_tableau1])
        indice_tableau1+=1
    while indice_tableau2<taille_tableau2:
        tableau_fusionne.append(tableau2[indice_tableau2])
        indice_tableau2+=1
    return tableau_fusionne


tableau = aleatoire(100)
print(tableau)
datetime.now()
before = datetime.timestamp(datetime.now())
tableau_trie = tri_fusion(tableau)
after = datetime.timestamp(datetime.now())
print(before)
print(after)
print(timedelta(before, after))
print(tableau_trie)