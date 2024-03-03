
hauteur = int( input("hauteur de la pyramide> ") )
if(hauteur < 1):
  print("hauteur invalide 🙊")
  exit(-1)

symbole = input("symbole de la pyramide> ")
if(len(symbole) != 1):
  print("symbole invalide 🙊")
  exit(-2)

pyramide = ""
for etage in range(1, hauteur + 1):
    pyramide += " " * (hauteur - etage) + symbole * (etage * 2 - 1) + "\n"
print(pyramide)
