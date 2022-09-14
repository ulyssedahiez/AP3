# Exercice 1 :

def NombresPremiers():
    entier = int(input("entrez un entier :"))
    
    tab = []
    iter = 1
    while len(tab) != entier:
        count =1
        for i in range(1, iter):
             
            if iter%i == 0:
                count+=1    
            if iter%i == iter:
                count += 1    
        if count <= 2:
            tab.append(iter)
        iter +=1
    print(tab)

#NombresPremiers()

#Exercice 2

def tablesmulti(der):
    tab = []
    for i in range(0, der):
        tab=[]
        for j in range(0,10):
            tab.append(i*j)
           
        print(tab)


#tablesmulti(5)

#Exercice 3


tab = [1.5,5.7,9.8,8.65,4.4,8.0,2.7,5.9,4.9,1.0,5.78,8.8,4.0,4.9,2.8,78.7,98.0,85.9,6.4,5.9]

def inf(a):
    tabl= []
    for i in range(0, len(tab)):

        if i > tab[i]:
            tabl.append(tab[i])
    return tabl

#print(inf(5))

def moysom(tabl):
    som = 0
    for i in range(0, len(tabl)):
        som+= tabl[i]
    moy = som/len(tabl)

    return {"somme":som, "moyenne":moy}



#print(moysom(tab))



def tronqu(tabl):
    tal = []
    for i in range (0, len(tabl)):
        x, y = str(tabl[i]).split(".")
        tal.append(int(x))

    return tal

#print(tronqu(tab))

def paire(tabl):
    res = []
    for i in range(0, len(tabl)):
        if (tabl[i]%2 == 0):
            res.append(tabl[i])
    return res

#print(paire(tab))


# Exercice 4

phraseCible = ["isen", "all", "is", "digital", "engineering"]

def itoj(tabl):
    res = []
    for i in range(0, len(tabl)):
        mot = ""
        for j in range(0, len(tabl[i])):

            if tabl[i][j] == "i":

                mot = mot+"j"
            else:
                mot=mot+tabl[i][j]
        print(mot)

        res.append(mot)
            
    return res


#print(itoj(phraseCible))

#Exercice 5

def pointscrable(mot):
    dico = {"A":1,"E":1,"I":1,"O":1,"U":1,"R":1,"N":1,"T":1,"L":1,"S":1,"D":2,"G":2,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}
    res = 0
    for i in range(0, len(mot)):

        res += dico[mot[i].upper()]
    print("le mot \"", mot, "\" vaut", res)

#pointscrable("Anticonstitutionnellement")

def tribulle(tabl):
    
    temp=0
    for i in range(0, len(tabl)):
        for j in range(0, len(tabl)):
            if tabl[i]<tabl[j]:
                temp = tabl[j]
                tabl[j]= tabl[i]
                tabl[i] = temp
    print(tabl)
         

#tribulle(tab)   

# Exercice 7
listbin = [1,25,54,87,60,2,5,78,14,12,35,5,45,65,254,69,85,2236,6955,7]

def suppbin(tabl):
    print(tabl)
    tabres = []
    for i in range(0, len(tabl)):
        valbin = bin(tabl[i])
        if (valbin[2::].count("0")<valbin[2::].count("1")):
            tabres.append(tabl[i])
    print(tabres)


#suppbin(listbin)

# Exercice 8
def possibilites_score_200():
    victoire = 50
    egalite = 20
    defaite = 0

    possibilites = []

    nb_parties = 10
    for nb_victoires in range(0, nb_parties + 1):
        for nb_egalites in range(0, nb_parties - nb_victoires + 1):
            for nb_defaites in range(0, nb_parties - nb_victoires - nb_egalites + 1):
                if nb_parties - nb_victoires - nb_egalites - nb_defaites == 0:
                    score = nb_victoires * victoire + nb_egalites * egalite + nb_defaites * defaite
                    if score == 200:
                        possibilites.append((nb_victoires, nb_egalites, nb_defaites))
    return possibilites

    


