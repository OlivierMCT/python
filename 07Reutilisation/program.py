from mathematiques import *
import bonjour
import bonjour as b
from bonjour import disBonjour


def gererBonjour():
    bonjour.disBonjour(salutation="Salut", question="Qui es-tu ? ")
    b.disBonjour("Prenom: ", "Bonjour")
    disBonjour()
    disBonjour("Comment tu t'appelles ? ")
    disBonjour(salutation="Coucou")
    disBonjour(salutation=11)


def gererMaths():
    nb = int(input("un nombre ? "))
    carre = calculerCarre(nb)
    print(nb, "² = ", carre, sep="")
    print(nb, "+ 20 =", additionner(nb, 20))
    print(nb, "+ 20 + 30 =", additionner(nb, 20, 30))
    print(nb, "- 20 =", soustraire(nb, 20))
    print(nb, "- 20 - 30 =", soustraire(nb, 20, 30))
    print(nb, "* 20 =", multiplier(nb, 20))
    print(nb, "* 20 * 30 =", multiplier(nb, 20, 30))
    print(nb, "* 20 * 30 * 40 =", multiplier(nb, 20, 30, 40))
    print(nb, "* 20 * 30 * 40 * 50 =", multiplier(nb, 20, 30, 40, 50))
    #print(nb, "* 20 * 30 * 40 * 50 =", multiplier(nb, 20, (30, 40, 50)))
    produit, partieEntiere, reste = diviser(nb, 20)
    print(nb, "/ 20 =", produit, " PE =", partieEntiere, " R =", reste)
    print(nb, "! = ", calculerFactorielle(nb), sep="")
    print(nb, "! = ", calculerFactorielleBis(nb), sep="")



print("Début de programme")
# gererBonjour()
gererMaths()
print("Fin de programme")
