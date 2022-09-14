def enleverVal(tab, ty):

    for i in range (0,len(tab)-2):
       
        if(tab[i]==ty):
            del tab[i]
    return tab

#enleverVal([1,6,5,2,1,4,7,5,6,4,2,9,8,1,6], 6)


def melange(w1, w2):
    
    if(w2 == ""):
        return w1
    if(w1 == ""):
        return w2
    else:
        return w1[0]+w2[0]+melange(w1[1:] ,w2[1:])
        


print(melange("hello", "world"))