import copy
a = [2,5,12,23,8,68,32,2,5,6,8,68]
print(len(a))


def supDoublonTableau(tabl):
    result = [tabl[0]] # on met un première valeur a result pour avoir un rang supérieur à 0
    for i in tabl: 
        n = 0
        trouve = False
        for n in range(len(result)): 
            if result[n] == i: #On cherche partout dans n la valeur de chaque nombre du tableau en entrée
                trouve = True #si on trouve un nombre égal on le signal comme trouvé
        if trouve == False: 
            result.append(i) #si le nombre n'a pas été trouvé dans la liste on l'ajoute dans le resultat
    return result

print(supDoublonTableau(a))