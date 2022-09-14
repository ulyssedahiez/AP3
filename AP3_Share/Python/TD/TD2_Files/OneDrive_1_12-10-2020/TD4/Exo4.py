
def TrieBulle(list):
    compteur = 0
    for index in range(len(list)-1):
        if list[index] > list[index + 1]:
            list[index],list[index + 1] = list[index + 1],list[index]
            compteur += 1
    if compteur == 0:
        return list
    else:
        return TrieBulle(list)

arr = [1,5,2,7,3]
print(TrieBulle(arr))