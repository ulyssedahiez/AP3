# exercice 1

def impaire(n):
    if(n%2 == 0):
        print(n, " pair")
    else:
        print(n, " impair")


def rectangleetoile(n):
    for i in range (0,n):
        print("*****")

#rectangleetoile(6)


def carreEtoile(n):
    stre = ""
    for i in range (0,n):
        stre = stre+" *"
    for j in range (0,n):
        print(stre)
    
carreEtoile(10)

# exercice 2

def maFonction(n):                                                
    lines=[[1],[1,1]]
    for i in range(2,n):
        taille = len(lines[-1])
        newLine = [1]
        for i in range(taille-1):
            newLine.append(lines[-1][i]+lines[-1][i+1])
        newLine.append(1)
        lines.append(newLine)
    for j in range(len(lines)):
        print(lines[j])
    return 

maFonction(10)




