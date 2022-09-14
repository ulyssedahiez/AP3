import random 
nombre = int(input("Entrez votre nombre : "))
tab = []
for i in range (nombre):
    tab.append(random.randint(1, 100))
print(tab)


