a= [1.23,3.7,5.43,8.69,1.5] 

def moyenneTab(tab):
    result=0
    for i in tab: # on additionne toutes les valeurs du tableau
      result += i
    if result != 0:
        result = result / len(tab) #si la valeur du tableau n'est pas de 0 on le divise par sa longueur pour avoir sa moyenne
    else:
        result = 0 # si la valeur du tableau vaux 0
    return result
print(moyenneTab(a))
