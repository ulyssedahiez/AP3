a = [2, 5, 12, 23, 8, 68, 32]

def supElementPairs(tabl):
    result = []
    for i in tabl:
       if i % 2 != 0:      #cherche dans le tableau tout les élements non pairs et les ajoutes au tableau result[]
           result.append(i)
    return result
    
print(supElementPairs(a))


