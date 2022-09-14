from random import randrange

def genererTalbleau(l):
    tab = []
    for i in range(0,l):
        tab.append(randrange(0,l))
    return tab



def triBul(tab):
    for i in range(len(tab)-1,0,-1 ):
        for j in range(0, i):
            if(tab[j+1]<tab[j]):
                val = tab[j]
                tab[j]=tab[j+1]
                tab[j+1]=val
    return tab

def triRapide(tab):

    return tab

print(triBul([7,5,2,8,4,2]))

