tab = []
nbrNombre = int(input("Nombre de nombre que vous voulez saisir: "))

def stockage(nombre, tab):
    if nombre >= 0:
        tab.append(nombre)
        print("Le nombre est bien stocké")
        return (tab)
    else:
        sys.exit()
        return (tab)

for index in range(nbrNombre):
    tab = stockage(float(input("Entrez un nombre:")), tab)
print(tab)
