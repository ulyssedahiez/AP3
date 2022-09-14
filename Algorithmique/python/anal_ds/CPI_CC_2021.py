
#

def tables(): # programme qui retourne toute les resultats des divisions de un à 10
    chaine = ""
    for i in range(1,10): # première boucle qui prend tout les nombre de un à 10
        for j in range(0,10): # deuxième boucle qui prend tout les nombres de la boucles precedente et les multiplie par 10
            chaine+= str(i*j)+" " #ajoute à la chaine 
        print(chaine) #affiche la chaine 
        chaine="" # réinitialise la chaine 

#tables()


def divisor(integer):
    chaine = ""
    for i in range(1, integer+1):
        if (not integer%i):
            chaine += str(i)+" "
    print (chaine)

divisor(30)

def counterForE(word):
    count = 0
    for i in range(0,len(word)):
        if(str.upper(word[i]) == "E"):
            count += 1
    print("there is "+str(count)+" e or E in "+word)

def counterForER(word):
    count = 0
    for i in range(0,len(word)):
        if(str.upper(word[i]) == "E"):
            if(str.upper(word[i+1]) == "R"):
                count += 1
    print("there is "+str(count)+" er or ER in " + word)
"""
counterForE("Clever")
counterForER("Clever")
counterForE("Cerberus")
counterForER("Cerberus")
counterForE("erererer")
counterForER("erererer")
"""

def calculator():
    number1 = int(input("Please input the first number  :"))
    number2 = int(input("Please input the second number  :"))
    operateur = str(input("Please input the oparation  :"))

    if operateur == "m":
        print("result : ", number1*number2)
    if operateur == "a":
        print("result : ", number1+number2)
    if operateur == "l":
        print("result : ", number1-number2)
    if operateur == "d":
        if(number2 == 0):
            print("not possible to divide by 0")
        else:
            print("result : ", number1/number2)

#calculator()

def replace(list):

    for mot in range(0, len(list)):
        for letter in range(0, len(mot)):
            if(str.upper(list[mot][letter])=="E"):
                
                list[mot][letter]="3"

ex2List  =  [ "HEI" ,  "Engineers" ,  "for" ,  "the" ,  "world" ]

replace(ex2List)


