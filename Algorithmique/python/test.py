from re import match
from random import randrange
"""
reg = "[o0Oe]{3}"

print(match(reg, "oo"))
print(match(reg, "EEo"))
print(match(reg, "oOe"), "oOe".count("e"), "oOe".find("e"))

ListOC = [
    [(2,2)],
    [(1,1),(1,3),(3,1),(3,3)],
    [(1,2),(2,1),(2,3),(3,2)]
    ]
print(":: ", ListOC[2][0][0]," :: ", ListOC[2][1])

print("len : ",len("1122"))
stringo = "211121"
thecount = 2
print(stringo[1:3])
print(stringo[1: int(thecount)+1])

print("theCount : ", stringo.replace(stringo[1: thecount+1], ""))

for i in range(0,3):
    
    for j in range(0,3):
        print(i,j)
        if(i==2 and j==2):
            print("ca s'arret ?")
            break
            print("apres le brack")
    print("mais on est là")

tab = [(3,1),(2,2),(1,3)]

for i in tab:
    print(i[1])


if(tab[0]==(3,1) or tab[1]==(2,2)):
    print("merde")
if(tab[0]==(3,1) and tab[1]==(2,2)):
    print("merde")



wae = "x X x u"
print(wae[1])
myList = [".","x","X"]
for j in myList:
    print(j)
    wae = wae.replace(j,"e")
print(wae)


tab=""
for i in range(0,100):
    tab = tab + str(randrange(0,10))
print(tab)


lo = [[(2,2)],[(1,1),(1,3),(3,1),(3,3)],[(1,2),(2,1),(2,3),(3,2)]]
print(lo)
del lo[1][0]
print(lo)

for i in range (0,0):
    print("rien")
 """

tab = [0,1,2,3,4,5,6,7,8,9]
print(tab[:-3])