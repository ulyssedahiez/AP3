unPt = ["a","e","i","o","u","n","r","t","l","s"]
deuxPt = ["d","g"]
troisPt = ["b","c","m","p"]
quatrePt = ["f","h","v","w","y"]
cinqPt = ["k"]
huitPt = ["j","x"]
dixPt = ["q","z"]

liste_mot = ["mot","test","h","bonjour", "a", "equal","as","sort"]


def scrabble(chaine) : 
	compteur = 0
	for i in chaine : 
		if i in unPt : 
			compteur+=1
		if i in deuxPt : 
			compteur+=2
		if i in troisPt:
			compteur+=3
		if i in quatrePt : 
			compteur+=4 
		if i in cinqPt : 
			compteur+=5
		if i in huitPt : 
			compteur+=8
		if i in dixPt :
			compteur+=10
		
	return compteur 


print(sorted(liste_mot,key=scrabble))
input("tapez entrer")





