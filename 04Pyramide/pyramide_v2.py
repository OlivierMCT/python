from pyramidev2Lib import *

hauteur = int( input("hauteur de la pyramide> ") )
if(hauteur < 1):
  print("hauteur invalide 🙊")
  exit(-1)

symbole = input("symbole de la pyramide> ")
if(len(symbole) != 1):
  print("symbole invalide 🙊")
  exit(-2)


builders = [
  construirePyramide1, 
  construirePyramide2,
  construirePyramide3,
  construirePyramide4,
  construirePyramide5,
  construirePyramide6,
  construirePyramide7,
]

for b in builders:
  pyramide = b(hauteur, symbole)
  print("\n".join(pyramide))
  [print(lg) for lg in pyramide[-2::-1]]
