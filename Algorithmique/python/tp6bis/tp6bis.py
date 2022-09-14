from os import linesep


def AfficherListeEntier(Fichier):
    ListEntier = open(Fichier, "r")
    ListEntier5 = ListEntier.read()
    ListEntier.close()
    lines = ListEntier5.splitlines()
    for i in lines:
        tr = int(i)
        print(tr)
    
    return

AfficherListeEntier("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\tp6bis\\ListeEntier.txt")

def ecrireFichier():
    texte = ""
    everything = []
    while texte != "stop":
        everything.append(texte)
        texte = input("prochaine ligne : ")

    f = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\tp6bis\\exo2.txt")
    f.write('\n'.join(everything))
    f.close()
    return

def insererNum():
    f = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\tp6bis\\exo3.txt")
    contenu = f.read()
    f.close()
    if contenu[0:2] == "1 ":
        lines = contenu.splitlines()
        f = open("C:\\Users\\Ulysse Dahiez\\Documents\\AP3\\Algorithmique\\tp6bis\\exo3.txt")
        for el in lines:
            f.write(el[2:]+'\n')
        f.close()
    else:
        lines = contenu.splitlines()

    










