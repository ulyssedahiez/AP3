import os

fichier = open("fichier_ex2.txt", "a")
chaine = ""

while True:
    chaine = (input("Entrez du texte: "))
    if chaine != "stop":
        fichier.write(chaine+"\n")
    else:
        break
fichier.close()