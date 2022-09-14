#Proposez une fonction r ́ecursive qui calcule la factorielle d’un entier positif n donn ́e.

n = int(input("Quel est votre nombre ? "))

def recursive(n) :
    if n < 0 :
        return "Nous ne pouvons pas traiter des nombres négatifs"
    elif n < 2 :
        return 1
    else:
        return n*recursive(n-1)

print recursive(n)
