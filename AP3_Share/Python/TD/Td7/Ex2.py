chaine1 = "abc"
chaine2 = "bcd"

chaine3 = "aaa"
chaine4 = "abd"

chaine5 = "bcd"
chaine6 = "efg"



def caractEnCommun(chaine1, chaine2):
    tabl1 = []
    tabl2 = []
    result = []
    #Recuperation des chaine sous forme de tableaux
    #tabl1
    for n in range(len(chaine1)):
        tabl1.append(chaine1[n:n+1])
    print(tabl1)
    #tabl2
    for n in range(len(chaine2)):
        tabl2.append(chaine2[n:n+1])
    print(tabl2)
    
    for i in tabl1:
        trouve = False
        for z in range(len(tabl2)):
            if i == tabl2[z]:
                trouve = True
        if trouve == True:
            if len(result) == 0:
                result.append(i)
            else:
                for u in range(len(result)):
                    if i != result[u]:
                        result.append(i)
    return result
    
    
print(caractEnCommun(chaine1,chaine2))

print(caractEnCommun(chaine3,chaine4))

print(caractEnCommun(chaine5,chaine6))