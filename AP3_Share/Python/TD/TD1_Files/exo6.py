#Soit un entier n. 
# Si n est pair, on le divise par 2. Si n est impair, on calcule 3n + 1.

n = int(input("Votre nombre : "))
while n != 1:
    print(n)
    if n%2 == 0:
        n = n//2
    else:
        n = 3*n + 1

print 1