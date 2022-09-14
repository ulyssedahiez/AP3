import copy
a = [2,5,12,23,8,68,32]
b = [1,2,23,6,68,24]



def tabSansDoublons(tab1,tab2):
    tabresult = copy.deepcopy(tab1)
    for i in tab2:
        if(i not in tab1):
           tabresult.append(i)
    return tabresult

print(tabSansDoublons(a,b))


    
