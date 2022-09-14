import random

def lanceDes():
    lances = []
    nombredees = int(input("entrez le nombre de dés que vous souhaitez lancer : "))
    for i in range(nombredees):
        lances.append(random.randint(1, 6))
    print(lances)
    
    maximal = 0
    for i in range(nombredees-1):
        if lances[i] > maximal:
            maximal = lances[i]
    print(maximal)
     
    iteration = 0
    suplement = 0  
    for i in range(1,maximal):
        iteration = 0
        for n in lances:
            if i == n:
                iteration +=1
        if iteration > 1:
            suplement += iteration - 1
    print(suplement)
    print("resultat final:",maximal+suplement)


lanceDes()