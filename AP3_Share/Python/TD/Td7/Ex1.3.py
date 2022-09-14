a = ["franc", "saucisse", "chauve", "funiculaire", "technocratie", "tramway"]

print(a)


def cherchePositionTableau(tabl):
    trouve = False
    val = str(input("entrez le mot pour récuperer sa position: "))
    for i in tabl:
        if val == i: #recherche si la valeur entrée est égale à chaque terme du tableau
           print("La valeur", i, "est en position :", tabl.index(i))
           trouve = True
    if trouve == False:
        print("acune position trouvé: -1")

cherchePositionTableau(a)