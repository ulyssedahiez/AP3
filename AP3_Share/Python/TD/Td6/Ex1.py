import os

fichier = open("fichier_ex1.txt", "r")

for line in fichier:

    if(int(line) >= 0):

        line = str(line)
        print(line.replace("\n", ""))
fichier.close()
