import random 
nombre = int(input("Entrez votre nombre : "))
tab = []
for i in range (nombre):
    tab.append(random.randint(1, 100000))
print(tab)


def mergesort(arr):

    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    a = mergesort(arr[:middle])
    b = mergesort(arr[middle:])
    return merge(arr, a, b)

def merge(arr, a, b):

    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return arr

print(mergesort(tab))