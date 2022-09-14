a = ["franc", "saucisse", "chauve", "funiculaire", "technocratie", "tramway"]

def ajoutElementPositionTableau(tabl):
    print("le tableau",tabl,"a une longueur de",len(tabl)-1,"éléments :")
    print("\nchoisissez une valeur comprise entre 0 et",len(tabl),":")
    position = int(input())
    element = str(input("\nchoisissez une valeur que vous voulez rentrez dans le tableau :"))
    if position > len(tabl):
        print("la valeur donné est supérieur à la position maximale, votre élément seras placé en dernier à la position",len(tabl))
    tabl.insert(position,element)
    print(tabl)
                  

ajoutElementPositionTableau(a)