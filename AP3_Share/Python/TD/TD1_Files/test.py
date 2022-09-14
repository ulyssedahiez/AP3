def scoreboard(q):
    p1 = ['A','E','I','O','U','N','R','T','L','S']
    p2 = ['D','G']
    p3 = ['B','C','M','P']
    p4 = ['F','H','V','W','Y']
    p5 = ['K']
    p8 = ['J','X']
    p10 = ['Q','Z']
    #n= str(input("Ecrire un mot ")).upper()
    score=0
    for i, c in enumerate(q):
        if c in p1:
            score = score+1
        elif c in p2:
            score = score+2
        elif c in p3:
            score = score+3
        elif c in p4:
            score = score+4
        elif c in p5:
            score = score+5
        elif c in p8:
            score = score+8
        elif c in p10:
            score = score+10
    return score
 
def tri():
    n= str(input("Ecrire une phrase ")).upper()
    split = n.split(" ")
    print (sorted(split, key=scoreboard))
        
tri()