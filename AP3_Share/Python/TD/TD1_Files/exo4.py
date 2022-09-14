#Proposez un programme qui convertisse en binaire, puis en h ́exad ́ecimal, un entier donn ́e.

n = int(input("Quel est votre nombre ? "))

def decToBin(n):
    if n==0: 
        return ''
    else:
        return decToBin(n/2) + str(n%2)

print decToBin(n)




#correction Prof
#def intoBin(n) :
#    if(n==0 or n==1)
#        return str(n)
#    else:
#        r = n%2
#       return (intoBin(n//2) + str(n))
# a = int(input())
#print(intoBin(a))