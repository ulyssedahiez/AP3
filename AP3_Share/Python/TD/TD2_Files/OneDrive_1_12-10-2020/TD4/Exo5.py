def Coef(point1, point2):
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    if (y1 - y2) == 0:
        return x1 - x2
    return (x1 - x2) / (y1 - y2)


nbrPoint = int(input("nombre de point"))

listPoint = []

for index in range(nbrPoint):
    x = float(input("abscisse"))
    y = float(input("ordonnée"))
    listPoint.append((x, y))

coef = Coef(listPoint[0], listPoint[1])
appartientTous = True

for index in range(1, len(listPoint)):
    var = Coef(listPoint[0], listPoint[index])
    if coef != Coef(listPoint[0], listPoint[index]):
        appartientTous = False
        break

if not appartientTous:
    print("Tout les points n'appartiennent pas a la droite")