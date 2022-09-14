import os


file = open("fichier_ex3.txt","r") 
tabl = ""
i = 1
for line in file:
    tabl= tabl+str(i)+". "+line
    i += 1
print(tabl)
file.close()

file = open("fichier_ex3.txt","w")
file.write(tabl)
file.close()
