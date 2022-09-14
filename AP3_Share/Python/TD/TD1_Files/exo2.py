#Soit le polynome suivant : ax2 + b ∗ x + c. 
#Proposez un programme qui calcule les diff ́erentes solutions possibles `a l’ ́equation a ∗ x2 + b ∗ x + c = 0.

from math import *
import sys

a = int(input("Entrez votre nombre a : "))
b = int(input("Entrez votre nombre b : "))
c = int(input("Entrez votre nombre c : "))

def calculDelta(a,b,c) :
    delta = b*b-4*a*c
    return delta

retourDelta = calculDelta(a,b,c)

if(a == 0) :
    solution = -c/b
    print "La solution de l'équation est : ", solution
elif(retourDelta == 0) :
    solutions = -b/2*a
    print "L'unique solution de l'équation est : ", solutions
elif(retourDelta > 0) :
    solutiona = (-b+sqrt(retourDelta))/2*a
    solutionb = (-b-sqrt(retourDelta))/2*a
    print "La première solution de l'équation est ", solutiona
    print "La deuxième solution de l'équation est ", solutionb
else :
    print "La solution n'a pas de solutions réelles"
