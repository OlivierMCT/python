def construirePyramide1(hauteur: int, symbole: str) -> list:
  lignes = list()
  for i in range(1, hauteur + 1):
    lignes.append((" " * (hauteur - i)) + (symbole * (i * 2 - 1)))
  return lignes

def construirePyramide2(hauteur: int, symbole: str) -> list:
  return list(map(lambda i:(" " * (hauteur - i)) + (symbole * (i * 2 - 1)), range(1, hauteur + 1)))

def construirePyramide3(hauteur: int, symbole: str) -> list:
  return [(" " * (hauteur - i)) + (symbole * (i * 2 - 1)) for i in range(1, hauteur + 1)]
  
def construirePyramide4(hauteur: int, symbole: str) -> list:
  def generateLine(nbSpaces, nbSymboles):
    return " " * nbSpaces + symbole * nbSymboles
  return [generateLine(hauteur - i, i * 2 - 1) for i in range(1, hauteur + 1)]

def construirePyramide5(hauteur: int, symbole: str) -> list:
  genererLigne = lambda nbSpaces, nbSymboles: " " * nbSpaces + symbole * nbSymboles
  return [genererLigne(hauteur - i, i * 2 - 1) for i in range(1, hauteur + 1)]

def construirePyramide6(hauteur: int, symbole: str) -> list:
  generateLine = lambda etage: " " * (hauteur - etage) + symbole * (etage * 2 - 1)
  return [generateLine(i) for i in range(1, hauteur + 1)]

def construirePyramide7(hauteur: int, symbole: str) -> list:
  return [
    (lambda etage: " " * (hauteur - etage) + symbole * (etage * 2 - 1))(i) 
    for i in range(1, hauteur + 1)
  ]