""" jeu du plus ou mois
trois essaie"""


import random

NOMBREMIN = 0
NOMBREMAX = 10
VIE = 3
joueur = -1
nombrejeu = random.randrange(NOMBREMIN,NOMBREMAX)
def choix_du_joueur (NOMBREMIN,NOMBREMAX):
    nombre_du_joueur = -1
    while nombre_du_joueur == -1 :
        try :
            nombre_du_joueur = int(input(f" donnez un nombre entre {NOMBREMIN} et {NOMBREMAX} ? "))
            if nombre_du_joueur < NOMBREMIN or nombre_du_joueur > NOMBREMAX:
                nombre_du_joueur = -1
            else :
                return nombre_du_joueur
        except :
            print ("bug")



def test_et_affiche(nbjoueur,nombrejeu) :
    if nbjoueur > nombrejeu : 
        print( "le nombre est plus petit")
        return False
    elif nbjoueur < nombrejeu : 
        print( "le nombre est plus grand")
        
        return False
    elif  nbjoueur == nombrejeu:
        return True
    else:
        return False

win = False
while VIE > 0 and win == False :
    nb =choix_du_joueur(NOMBREMIN,NOMBREMAX)
    win = test_et_affiche(nb,nombrejeu)
    VIE = VIE -1

if VIE == 0:
    print( f" vous avez perdu ! le nombre était {nombrejeu}")
else : 
    print("vosu avez gagner !")