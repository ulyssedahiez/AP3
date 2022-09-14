import os
import datetime
import time

file = open("fichier_ex4.txt", "r")
tab = file.readlines()
date1 = time.strptime(tab[0].replace("\n", ""), "%d/%m/%Y %H:%M")
date2 = time.strptime(tab[1].replace("\n", ""), "%d/%m/%Y %H:%M")
d1s = time.mktime(date1)
d2s = time.mktime(date2)
secondes = abs(d2s-d1s)
print(str(datetime.timedelta(seconds=secondes)))
