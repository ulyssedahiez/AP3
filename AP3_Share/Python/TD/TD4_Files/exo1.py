import os
import time
import datetime

def ex1():
    file = open("test.txt","r")
    for line in file:
        if(int(line)>=0):
            print(line)
    file.close()
    return


def ex2():
    file = open("data.txt","a")
    a = ""
    while(a != "STOP"):
        a = str(input("votre phrase: "))
        if a!= "STOP" :
            file.write(a + "\n")
    file.close()
    return


def ex3():
    file = open("data.txt","r") 
    tabl = ""
    i = 1
    for line in file:
        tabl= tabl+str(i)+". "+line
        i += 1
    file.close()
    
    file = open("data.txt","w")
    file.write(tabl)
    file.close()


def ex4():
    file= open("date.txt","r")
    tab=file.readlines()
    date1=time.strptime(tab[0].replace("\n",""), "%d/%m/%Y %H:%M")
    date2=time.strptime(tab[1].replace("\n",""), "%d/%m/%Y %H:%M")
    d1s=time.mktime(date1)
    d2s=time.mktime(date2)
    secondes=abs(d2s-d1s)
    print(str(datetime.timedelta(seconds=secondes)))



file = open("fichier_ex5.txt")
contenu = file.read()
line = contenu.split("\n")

"""fonction permettant de calculer quel est la plus grande chaine et ensuite tri à bulle sur la longueur d'une chaine line """
def PlusGrand():
    for i in range(0, len(line)):
        for cpt in range(0, len(line)-1):
            if(len(line[cpt]) > len(line[cpt+1])):
                temp = line[cpt]
                line[cpt] = line[cpt+1]
                line[cpt+1] = temp
    return line

def NoDouble(line, final, y):
    if(y < len(line)):
        if(line[y] in final):
            return NoDouble(line, final, y+1)
        else:
            final.append(line[y])
            return NoDouble(line, final, y+1)
    else:
        return final

def Main():
    line = PlusGrand()
    print(NoDouble(line, [], 0))

Main()
file.close()