p1 = [1,'A','E','I','O','U','N','R','T','L','S']
p2 = [2,'D','G']
p3 = [3,'B','C','M','P']
p4 = [4,'F','H','V','W','Y']
p5 = [5,'K']
p6 = [8,'J','X']
p7 = [10,'Q','Z']

n = str(input("Ecrire un mot ")).upper()
x= 0
score = 0
while x != len(n) :
    for c in enumerate(n) :
        if c in p1 :
            score = score + p1[0]
        if c in p2 :
            score = score + p2[0]
        if c in p3 :
            score = score + p3[0]
        if c in p4 :
            score = score + p4[0]
        if c in p5 :
            score = score + p5[0]
        if c in p6 :
            score = score + p6[0]
        if c in p7 :
            score = score + p7[0]

print(score)


def score(test) :
    