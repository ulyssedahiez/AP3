def sommeList(listEn):
    if(len(listEn)!=1):
        listEn[0]= listEn[0]+ listEn[1]
        listEn.pop(1)
        listEn = sommeList(listEn)
    return listEn

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n  * factorielle(n-1)

def plusGrandeValeurList(listVal):
    if(listVal[len(listVal)]<listVal[len(listVal)]):
        rec = listVal[0]
        listVal[0] = listVal[len(listVal)]
        listVal[len(listVal)] = rec
        listVal = plusGrandeValeurList(listVal)
    else:
        listVal = plusGrandeValeurList(listVal)
        return listVal

def nDoublons(liste):
    if len(liste):
        return liste
    liste_range = plusGrandeValeurList(liste)
"""
print("sommeList : ",sommeList([24,5,1998]))
print("factoriel : ", factorielle(5))
print("plusGrandeValeurList : ", plusGrandeValeurList([24,5,1998]))
"""

def triangle(strt, longueur):
    if(len(strt)==longueur):
        return strt
    elif(len(strt)==0):
        return triangle("1", longueur)
    else:
        print(strt)
        thecount = strt[0,len(str)].count(strt[0])
        strt = str(thecount)+strt
        return triangle(strt, longueur)
        


print("triangle", triangle("",7))

# correction 

import math
liste = [5,3,-10,25]

def recursomme(liste):
    if len(liste)==1:
        return liste[0] #condition d'arret
    else:
        return liste[0] + recursomme(liste[1:]) #pas

#print(recursomme(liste))

def recurfaco(n):
    if n == 1:
        return 1
    else:
        return n * recurfaco(n-1)

#print(recurfaco(5))

def recurtri(liste):
    print(liste)
    if len(liste)==1:
        return liste[:1]
    else:
        if liste[0]>liste[1]:
            return liste[:1]+recurtri(liste[1:])
        else:
            a=liste[0]
            liste[0]=liste[1]
            liste[1]=a
            return recurtri(liste)

def recurtri2(liste):
    n = len(liste)
    if n==1:
        return liste
    else:
        return recurtri2(recurtri(liste)[:n-1])

#print(recurtri2(liste))


def greatest_rec(list):
    if (len(list)==1):
        return [list[0]]
    else:
        if (list[1]<list[0]):
            tmp = list[0]
            list[0] = list[1]
            list[1] = tmp
        return greatest_rec(list[1:])+[list[0]]



def nDoublons(liste):
    if len(liste)==1:
        return liste
    liste_rangee = greatest_rec(liste)
    liste_rangee2 = list({liste_rangee[0]}) + greatest_rec(liste_rangee[1:])
    if liste_rangee2[0] != liste_rangee2[1]:
        return list({liste_rangee2[0]})+nDoublons(liste_rangee2[1:])
    else:
        return nDoublons(liste_rangee2[1:])

#print(nDoublons([1,5,10,5]))

def intToString(i):
    if i == 0:
        return
    if i<0:
        print("-", end="")
        intToString(-i)
        return
    intToString(math.floor(i/10))
    print(i-math.floor(i/10)*10, end="")
    return

#intToString(1354)

#Ex 2

def scores(liste,a):
    if a<0 or len(liste)>10:
        return
    if a==0 and len(liste)==10:
        print(liste)
        return
    scores(liste+[0],a)
    scores(liste+[20],a-20)
    scores(liste+[50],a-50)
    return

scores([],200)
