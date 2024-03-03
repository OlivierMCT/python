from pyramide_class_v3 import *

hauteur = -1
while True:
    try:
        hauteur = int(input("hauteur de la pyramide> "))
        if(hauteur < 1):
            print("hauteur invalide 🙊")
        else:
            break
    except ValueError as err:
        print("hauteur non numérique 🙊")

symbole = ""
while True:
    symbole = input("symbole de la pyramide> ")
    if(len(symbole) != 1):
        print("symbole invalide 🙊")
    else:
        break

try:
    p = pyramide(hauteur, symbole)
    print(p)
    [print(lg) for lg in p.genererEtages()[-2::-1]]

except:
    print("Pas bien !")
