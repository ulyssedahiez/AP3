import random 
nombre = int(input("Entrez votre nombre : "))
tab = []
for i in range (nombre):
    tab.append(random.randint(1, 100))
print(tab)


def TrieBulle(list):
    compteur = 0
    for index in range(len(list)-1):
        if list[index] > list[index + 1]:
            list[index],list[index + 1] = list[index + 1],list[index]
            compteur += 1
    if compteur == 0:
        return list
    else:
        return TrieBulle(list)

print(TrieBulle(tab)) 
