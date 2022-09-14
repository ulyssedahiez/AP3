file = open("fichier_ex5.txt")
contenu = file.read()
line = contenu.split("\n")

def PlusGrand():
    '''
        fonction permettant de calculer quel est la plus grande chaine 
        et ensuite tri à bulle sur la longueur d'une chaine

        line 
    '''
    for i in range(0, len(line)):
        for cpt in range(0, len(line)-1):
            if(len(line[cpt]) > len(line[cpt+1])):
                temp = line[cpt]
                line[cpt] = line[cpt+1]
                line[cpt+1] = temp
    return line

def NoDouble(line, final, y):
    '''
        Fonction empechant les doublons 
    '''
    if(y < len(line)):
        if(line[y] in final):
            return NoDouble(line, final, y+1)
        else:
            final.append(line[y])
            return NoDouble(line, final, y+1)
    else:
        return final

def Main():
    line = PlusGrand()
    print(NoDouble(line, [], 0))

Main()
file.close()