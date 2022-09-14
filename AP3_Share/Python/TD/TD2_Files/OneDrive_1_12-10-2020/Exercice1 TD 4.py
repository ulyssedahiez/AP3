tableau = []

a=0

def tableau_f(a):
    a = int(input())
    if a<0:
        tableau.append(a)
        print(tableau)
        tableau_f(a)
    else:
        return
tableau_f(a)
